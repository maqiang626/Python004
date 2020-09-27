#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04B17901 maqiang <maqiang626@qq.com> [2020-09-27 21:16 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 1. 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间
# 2. 并以 UTF-8 字符集保存到 csv 格式的文件中
# 3. 猫眼电影网址： https://maoyan.com/films?showType=3
# 4. 要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
#
# ==================================================================
#

import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem
from time import sleep


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        # Debug
        print('==================================================================')
        print(f'01 返回值：{response.text}')
        print(f'02 返回地址：{response.url}')

        count = 0
        items = []

        movies = Selector(response=response).xpath(
            '//div[@class="movie-hover-info"]')
        for movie in movies:
            divs = movie.xpath('./div[@class="movie-hover-title"]')
            movie_name = divs[0].xpath('./span[@class="name "]/text()').get()
            movie_type = divs[1].xpath('./text()').getall()[1].strip()
            movie_releasetime = movie.xpath(
                './div[@class="movie-hover-title movie-hover-brief"]').xpath('./text()').getall()[1].strip()

            count += 1
            if count == 11:
                break

            # Debug
            print('--------------------------------------------------------')
            print(
                f'03 电影信息：{count} {movie_name} {movie_type} {movie_releasetime}')

            item = MaoyanmovieItem()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_releasetime'] = movie_releasetime
            items.append(item)

            sleep(5)

        return items
