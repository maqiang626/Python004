# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()                 # 数据库表字段 id (uuid)
    movie_name = scrapy.Field()         # 电影名称
    movie_type = scrapy.Field()         # 电影类型
    movie_releasetime = scrapy.Field()  # 上映时间
