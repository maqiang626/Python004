# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        with open('./maoyanmovie_20200927.csv', 'a+', encoding='utf-8') as mym:
            mym.write(
                f'{item["movie_name"]},{item["movie_type"]},{item["movie_releasetime"]}\n')
        return item
