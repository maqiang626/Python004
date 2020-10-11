#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v2.0 04B27902 maqiang <maqiang626@qq.com> [2020-10-11 18:18 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# [+] 为 Scrapy 增加代理 IP 功能
# [+] 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制
# [+] 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库
# [+] item 增加 id 属性 (对应数据库表字段)
# [-] 去除 start_urls (已经使用了 start_requests)
# [-] parse 方法去除 sleep 方法 (页面内容已下载)
# [-] 去除调试相关代码
# [-] 去除 items
# [*] 优化计数方法，去除 count 计数，直接使用 for 循环方法替代
# [*] movie_name 优化判断规则
#
# ==================================================================
#

import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem
import uuid


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        try:
            movies = Selector(response=response).xpath(
                '//div[@class="movie-hover-info"]')
            for movie in movies[:10]:
                divs = movie.xpath('./div[@class="movie-hover-title"]')
                movie_name = divs[0].xpath(
                    './span[@class="name "]/text()').get()
                if not movie_name:
                    movie_name = divs[0].xpath(
                        './span[@class="name noscore"]/text()').get()
                movie_type = divs[1].xpath('./text()').getall()[1].strip()
                movie_releasetime = movie.xpath(
                    './div[@class="movie-hover-title movie-hover-brief"]').xpath('./text()').getall()[1].strip()

                item = MaoyanmovieItem()
                uuid5 = str(uuid.uuid5(uuid.NAMESPACE_DNS, movie_name))
                item['id'] = ''.join(uuid5.split('-'))  # 对应数据库表字段 id (uuid)
                item['movie_name'] = movie_name
                item['movie_type'] = movie_type
                item['movie_releasetime'] = movie_releasetime

                yield item
        except Exception as e:
            print(f'页面下载异常：{e}')
