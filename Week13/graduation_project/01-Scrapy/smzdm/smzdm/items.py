# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmzdmItem(scrapy.Item):
    title = scrapy.Field()
    alink = scrapy.Field()
    comment = scrapy.Field()
    crawling_date = scrapy.Field()
