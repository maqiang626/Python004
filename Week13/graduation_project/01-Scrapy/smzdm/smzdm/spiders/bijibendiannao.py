import scrapy
from scrapy.selector import Selector
from smzdm.items import SmzdmItem
from time import sleep
from datetime import datetime
import random


class BijibendiannaoSpider(scrapy.Spider):
    name = 'bijibendiannao'
    allowed_domains = ['smzdm.com']

    def start_requests(self):
        url = f'https://www.smzdm.com/fenlei/bijibendiannao/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        '''爬取前 10 产品相关信息
        '''

        ul = Selector(response=response).xpath(
            '//*[@id="feed-main-list"]/li[position()<11]')

        for li in ul:
            item = SmzdmItem()
            alink = li.xpath('./div/div[2]/h5/a/@href')[0].get()
            title = li.xpath('./div/div[2]/h5/a/text()')[0].get()
            item['title'] = title
            item['alink'] = alink
            item['comment'] = []
            item['crawling_date'] = []

            sleep(random.randint(1, 3))

            yield scrapy.Request(url=alink, meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):
        """爬取评论数量和分页相关信息
        """

        item = response.meta['item']

        pagination = Selector(response=response).xpath(
            '//div[@id="comment"]/div[1]/ul[@class="pagination"]/li/a/@href').extract()
        comment_num = Selector(response=response).xpath(
            '//em[@class="commentNum"]')

        # 每页 30 条评论，存在无评论或多页评论情况
        if comment_num == 0:  # 无评论
            item['comment'] = []
            item['crawling_date'] = datetime.now().strftime('%Y-%m-%d')
            yield item
        else:  # 有评论
            if not pagination:  # 单页评论
                selectors = Selector(response=response).xpath(
                    '//div[@id="commentTabBlockNew"]/ul/li/div[2]/div[2]/div[1]')
                for span in selectors:
                    item['comment'] = span.xpath(
                        './p/span/text()').extract_first()
                    item['crawling_date'] = datetime.now().strftime('%Y-%m-%d')
                    yield item
            else:  # 多页评论
                for page in pagination[:-2]:
                    sleep(random.randint(1, 3))
                    yield scrapy.Request(url=page, meta={'item': item}, callback=self.parse_comment, dont_filter=True)

    def parse_comment(self, response):
        """爬取具体评论相关信息
        """

        item = response.meta['item']
        selectors = Selector(response=response).xpath(
            '//div[@class="comment_con"]')
        for span in selectors:
            item['comment'] = span.xpath('./p/span/text()').extract_first()
            item['crawling_date'] = datetime.now().strftime('%Y-%m-%d')
            yield item
