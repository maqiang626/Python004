# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SmzdmPipeline:
    def open_spider(self, spider):
        self.pymysql_connect = pymysql.connect(host='192.168.59.220',
                                               port=3306,
                                               user='root',
                                               password='MRP@Tmp59220',
                                               database='db_w13',
                                               charset='utf8mb4'
                                               )

    def process_item(self, item, spider):
        # 获得 cursor 游标对象
        connect_cursor = self.pymysql_connect.cursor()

        # 执行单条记录插入
        insert_sql = 'INSERT INTO tb_original_comments(title, alink, comment, crawling_date) values(%s, %s, %s, %s)'
        insert_value = (item["title"], item["alink"],
                        item["comment"], item["crawling_date"])
        connect_cursor.execute(insert_sql, insert_value)
        connect_cursor.close()

        return item

    def close_spider(self, spider):
        self.pymysql_connect.commit()
        self.pymysql_connect.close()
