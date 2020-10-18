#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B88501 maqiang <maqiang626@qq.com> [2020-10-18 23:20 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 1. 基于 selenium 和多线程方式进行网站内容的爬取
# 2. 获取北京、上海、广州、深圳四个地区，各地区 100 个 Python 工程师职位的职位名称和薪资水平
# 3. 相同地区、相同职位及相同待遇的职位需去重
# 4. 将获取的内容存入数据库中
# (选做) 使用图形库展示各地区 Python 工程师薪资分布情况，使用不同颜色代表该地区 Python 工程师薪资高低情况（建议使用 echart 或 matplotlib，具体图形库不限）
#
# ==================================================================
#

import random
from selenium import webdriver
from time import sleep
from lxml import etree
from queue import Queue
import time
import threading
import pymysql
import numpy as np
import matplotlib.pyplot as plt


class CrawlJobThread(threading.Thread):
    """多线程爬虫：获取页面
    """

    def __init__(self, crawl_thread, citys_queue):
        super().__init__()
        self.crawl_thread = crawl_thread
        self.citys_queue = citys_queue

    def run(self):
        print(f'{time.time()} 开始获取页面：{self.crawl_thread}')
        self.get_job()
        print(f'{time.time()} 完成获取页面：{self.crawl_thread}')

    def get_job(self):
        try:
            while not self.citys_queue.empty():
                browser = webdriver.Chrome()
                browser.get('https://www.lagou.com')
                sleep(3)

                # 按钮：[切换城市]
                city = self.citys_queue.get()
                browser.find_element_by_xpath(
                    f'//a[@data-city="{city}"]').click()

                # 文本输入框：搜索职位、公司或地点
                browser.find_element_by_id(
                    'search_input').send_keys('Python工程师')
                sleep(random.randint(1, 3))

                # 按钮：搜索
                browser.find_element_by_id('search_button').click()
                sleep(random.randint(2, 5))

                # 获取网页源代码
                pages_queue.put((city, browser.page_source))
                sleep(random.uniform(6, 9))

                # 按钮：下一页
                for _ in range(10):
                    btn_next = browser.find_element_by_xpath(
                        '//span[@class="pager_next "]')
                    browser.execute_script(
                        "arguments[0].click();", btn_next)
                    sleep(random.uniform(6, 11))
                    pages_queue.put((city, browser.page_source))
                    sleep(random.uniform(2, 6))

                sleep(random.randint(6, 26))

        except Exception as e:
            print(f'get_job Error: {e}')
        finally:
            browser.close()


class ParseJobThread(threading.Thread):
    """多线程：解析页面
    """

    def __init__(self, parse_thread, pages_queue):
        threading.Thread.__init__(self)
        self.parse_thread = parse_thread
        self.pages_queue = pages_queue

    def run(self):
        try:
            print(f'{time.time()} 开始解析页面：{self.parse_thread}')

            while True:
                page = self.pages_queue.get(False)
                self.parse_job(page)
                self.pages_queue.task_done()

            print(f'{time.time()} 完成解析页面：{self.parse_thread}')
        except:
            pass

    def parse_job(self, page):
        try:
            # 当前页面职位列表
            position_list = etree.HTML(page[1]).xpath(
                '//*[@id="s_position_list"]/ul/li')

            # 具体职位相关信息：city / name / salary
            for position in position_list:
                name = position.xpath('./div[1]/div[1]/div[1]/a/h3/text()')[0]
                salary = position.xpath(
                    'div[1]/div[1]/div[2]/div/span/text()')[0]
                job = (page[0], name, salary)

                low, high = salary.split('-')
                low = low[:-1]
                high = high[:-1]
                avg = int(low) + int(low) / 2

                # 去重：相同地区、相同职位及相同待遇的职位
                if job not in jobs_list:
                    jobs_list.append(job)
                    if page[0] == '北京':
                        salary_distribution['北京'][2] += 1
                        salary_distribution['北京'][3] += int(avg)

                        if int(low) < int(salary_distribution['北京'][0]):
                            salary_distribution['北京'][0] = low
                        if int(high) > int(salary_distribution['北京'][1]):
                            salary_distribution['北京'][1] = high
                    elif page[0] == '上海':
                        salary_distribution['上海'][2] += 1
                        salary_distribution['上海'][3] += int(avg)

                        if int(low) < int(salary_distribution['上海'][0]):
                            salary_distribution['上海'][0] = low
                        if int(high) > int(salary_distribution['上海'][1]):
                            salary_distribution['上海'][1] = high
                    elif page[0] == '广州':
                        salary_distribution['广州'][2] += 1
                        salary_distribution['广州'][3] += int(avg)

                        if int(low) < int(salary_distribution['广州'][0]):
                            salary_distribution['广州'][0] = low
                        if int(high) > int(salary_distribution['广州'][1]):
                            salary_distribution['广州'][1] = high
                    elif page[0] == '深圳':
                        salary_distribution['深圳'][2] += 1
                        salary_distribution['深圳'][3] += int(avg)

                        if int(low) < int(salary_distribution['深圳'][0]):
                            salary_distribution['深圳'][0] = low
                        if int(high) > int(salary_distribution['深圳'][1]):
                            salary_distribution['深圳'][1] = high

                sleep(0.2)
        except Exception as e:
            print(f'parse_job Error: {e}')


class StoreDB(object):
    """将获取的内容存入数据库中

    执行批量插入
    """

    def __init__(self, dbInfo, jobs_list):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.jobs_list = jobs_list

    def run(self):
        try:
            pymysql_connect = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            connect_cursor = pymysql_connect.cursor()

            # 执行批量插入
            connect_cursor.executemany(
                'INSERT INTO tb_job(city, name, salary) values(%s, %s, %s)', self.jobs_list)
            pymysql_connect.commit()

            connect_cursor.close()
        except:
            pymysql_connect.rollback()
        finally:
            pymysql_connect.close()


def plot_salary():
    """使用图形库展示各地区 Python 工程师薪资分布情况

    使用不同颜色代表该地区 Python 工程师薪资高低情况
    最低工资：绿色
    平均工资：黄色
    最高工资：红色
    """

    try:
        # 设置当前时间
        current_time = time.strftime('%Y-%m-%dT%H-%M-%S')

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
        plt.rcParams['savefig.dpi'] = 200             # 图片像素
        plt.rcParams['figure.dpi'] = 200              # 分辨率
        n_groups = 4

        # lowest(最低工资) / avg(平均工资) / hightest(最高工资)
        lowest = [int(salary_distribution['北京'][0]), int(salary_distribution['上海'][0]), int(
            salary_distribution['广州'][0]), int(salary_distribution['深圳'][0])]
        avg = [int(salary_distribution['北京'][3]) // int(salary_distribution['北京'][2]), int(salary_distribution['上海'][3]) // int(salary_distribution['上海'][2]),
               int(salary_distribution['广州'][3]) // int(salary_distribution['广州'][2]), int(salary_distribution['深圳'][3]) // int(salary_distribution['深圳'][2])]
        highest = [int(salary_distribution['北京'][1]), int(salary_distribution['上海'][1]), int(
            salary_distribution['广州'][1]), int(salary_distribution['深圳'][1])]

        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.2
        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        ax.bar(index, lowest, bar_width, alpha=opacity, color='g',
               error_kw=error_config, label='最低工资')

        ax.bar(index + bar_width, avg, bar_width, alpha=opacity, color='y',
               error_kw=error_config, label='平均工资')

        ax.bar(index + bar_width + bar_width, highest, bar_width,
               alpha=opacity, color='r', error_kw=error_config,
               label='最高工资')

        ax.set_xticks(index + 3 * bar_width / 3)
        ax.set_xticklabels(('北京', '上海', '广州', '深圳'))
        ax.legend()
        plt.xlabel(f'城市')
        plt.ylabel(f'工资 / 月 (K)')
        ax.set_title(f'Python 工程师薪资分布情况\n({current_time})', fontsize=16)

        # lowest: 为每个条形图添加数值标签
        for xlowest, ylowest in enumerate(lowest):
            plt.text(xlowest, ylowest+1, ylowest, ha='center', fontsize=16)

        # avg: 为每个条形图添加数值标签
        for xavg, yavg in enumerate(avg):
            plt.text(xavg+0.20, yavg+1, yavg, ha='center', fontsize=16)

        # highest: 为每个条形图添加数值标签
        for xhighest, yhighest in enumerate(highest):
            plt.text(xhighest+0.40, yhighest+1,
                     yhighest, ha='center', fontsize=16)

        fig.tight_layout()
        plt.savefig(f'plot_salary_{current_time}.png', dpi=200)
        plt.show()
    except Exception as e:
        print(f'Plot error: {e}')


pages_queue = Queue()  # 爬取的页面汇总
jobs_list = []         # Python 工程师职位列表汇总

# Python 工程师薪资分布情况 (最低工资 / 最高工资 / 职位总数 / 平均工资总额)
salary_distribution = {
    '北京': [100, 0, 1, 0],
    '上海': [100, 0, 1, 0],
    '广州': [100, 0, 1, 0],
    '深圳': [100, 0, 1, 0]
}

# 待爬取的城市列表
citys_queue = Queue()
citys_queue.put('北京')
citys_queue.put('上海')
citys_queue.put('广州')
citys_queue.put('深圳')


if __name__ == "__main__":
    # 多线程爬虫：获取页面
    crawl_threads = []
    crawl_thread_list = ['C1', 'C2', 'C3', 'C4']
    for crawl_thread in crawl_thread_list:
        thread = CrawlJobThread(crawl_thread, citys_queue)
        crawl_threads.append(thread)

    for cthread in crawl_threads:
        cthread.start()

    for cthread in crawl_threads:
        cthread.join()

    # 多线程：解析页面
    parse_threads = []
    parse_thread_list = ['P1', 'P2', 'P3', 'P4']
    for parse_thread in parse_thread_list:
        thread = ParseJobThread(parse_thread, pages_queue)
        parse_threads.append(thread)

    for pthread in parse_threads:
        pthread.start()

    for pthread in parse_threads:
        pthread.join()

    print(f'======================= {time.time()} =======================')
    print(f'len(jobs_list) {len(jobs_list)}')
    print(f'salary_distribution {salary_distribution}')

    # 将获取的内容存入数据库中
    dbInfo = {
        'host': '192.168.59.220',
        'port': 3306,
        'user': 'root',
        'password': 'Easyway@iPark59220',
        'db': 'db_week'
    }
    db = StoreDB(dbInfo, jobs_list)
    db.run()

    # 使用图形库展示各地区 Python 工程师薪资分布情况
    # 使用不同颜色代表该地区 Python 工程师薪资高低情况
    plot_salary()
