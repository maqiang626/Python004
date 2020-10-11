# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

pymysql_connect = pymysql.connect(host='192.168.59.220',
                                  port=3306,
                                  user='root',
                                  password='******',
                                  database='db_maoyan',
                                  charset='utf8mb4'
                                  )

# 获得 cursor 游标对象
connect_cursor = pymysql_connect.cursor()


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        # 执行单条记录插入
        insert_sql = 'INSERT INTO tb_maoyan_film(id, movie_name, movie_type, movie_releasetime) values(%s, %s, %s, %s)'
        insert_value = (item["id"], item["movie_name"],
                        item["movie_type"], item["movie_releasetime"])
        connect_cursor.execute(insert_sql, insert_value)
        pymysql_connect.commit()

        connect_cursor.close()
        pymysql_connect.close()

        return item
