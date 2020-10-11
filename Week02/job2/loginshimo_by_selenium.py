#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B38001 maqiang <maqiang626@qq.com> [2020-10-11 18:15 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 使用 Selenium 模拟登录石墨文档 https://shimo.im
#
# ==================================================================
#

from selenium import webdriver
from time import sleep


def login(url):
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        sleep(5)

        # 首页 - 登录 (按钮)
        browser.find_element_by_xpath(
            '//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
        sleep(5)

        # find_element_by_xpath (Copy XPath)
        # browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('13913103557')
        # browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('******')
        # browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

        # 输入注册手机号或邮箱
        browser.find_element_by_xpath(
            "//input[@name='mobileOrEmail']").send_keys('13913103557')
        sleep(2)

        # 输入密码
        browser.find_element_by_xpath(
            "//input[@name='password']").send_keys('******')
        sleep(3)

        # 立即登录
        # 出现验证码，需手动验证通过
        browser.find_element_by_class_name('sm-button').click()
        sleep(56)

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == "__main__":
    login('https://shimo.im/')
