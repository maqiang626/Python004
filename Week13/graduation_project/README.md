# Week13 期末作业 (2020.12.21 - 2020.12.27)



# 第十三周：期末作业




# 毕业项目

**毕业项目：**构建一个舆情分析平台



**项目背景：**某公司计划新上线一款苏打水饮料，为了了解用户对苏打水的接受程度，需要抓取“什么值得买”([ https://www.smzdm.com/fenlei/qipaoshui/ ](https://www.smzdm.com/fenlei/qipaoshui/)) 网站中气泡水种类前 10 的产品的用户评论，通过对用户评论的正向、负向评价了解排名前 10 的气泡水产品的用户接受程度。



**注意：**
 由于这个网站的产品是实时更新的，一些新的气泡水产品可能没有足够数量的评论，大家可以将气泡水替换为其他产品，比如：

- 手机产品 24 小时排行 [ https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/ ](https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/)
- 电脑游戏最新排行 [ https://www.smzdm.com/fenlei/diannaoyouxi/ ](https://www.smzdm.com/fenlei/diannaoyouxi/)
- 洗发护发产品 24 小时排行 [ https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/ ](https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/)



**具体需求：**

1. 正确使用 Scrapy 框架或 Selenium 获取评论，如果评论有多页，需实现自动翻页功能，将原始评论结果存入 MySQL 数据库，并使用定时任务每天定期更新。
2. 对评论数据进行清洗（可借助 Pandas 库），并进行语义情感分析，将分析结果存入数据库。
3. 使用 Django 集成在线图表对采集数、舆情进行展示，需包括该产品正、负评价比例，以及评价内容等。
4. 数据展示支持按时间筛选和按关键词筛选功能（参考 [ https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817）。](https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817）。)



**评分标准：**（实现相应功能，每项 +10 分，部分实现 +5 分）

1. 正确使用 Scrapy 框架获取评论，如果评论有多页，需实现自动翻页功能。
2. 评论内容能够正确存储到 MySQL 数据库中，不因表结构不合理出现数据截断情况。
3. 数据清洗后，再次存储的数据不应出现缺失值。
4. Django 能够正确运行，并展示采集到的数据，数据不应该有乱码、缺失等问题。
5. 在 Django 上采用图表方式展示数据分类情况。
6. 舆情分析的结果存入到 MySQL 数据库中。
7. 在 Django 上采用图表方式展示舆情分析的结果。
8. 可以在 Web 界面根据关键字或关键词进行搜索，并能够在页面展示正确的搜索结果。
9. 支持按照时间（录入时间或评论时间）进行搜索，并能够在页面展示正确的搜索结果。
10. 符合 PEP8 代码规范，函数、模块之间的调用高内聚低耦合，具有良好的扩展性和可读性。





# 项目解析说明

## 00-SQL

`PIP-requirements`  依赖包

- `requirements.txt`



`db_w13.sql`  数据库导出脚本文件

- `tb_original_comments`     原始评论相关信息
- `tb_semantic_emotion`       经过数据清洗和语义情感分析后的评论相关信息
- `tb_sentiment_analysis`   舆情分析结果



## 01-Scrapy

- 爬取“**什么值得买**”网站中“**笔记本电脑**”分类的“**24小时排行**”信息
- 爬取前 `10` 产品相关信息
- 爬取评论数量和分页相关信息
- 爬取具体评论相关信息
- 所有原始评论数据存入 `MySQL` 数据库



## 02-Pandas

- 从数据库中获取原始评论数据
- 对评论数据进行清洗
  - 去除重复值
  - 去除缺失值
- 对清洗后的数据进行语义情感分析
- `DataFrame` 数据（经过语义情感分析后的数据）存入数据库
- 舆情分析的结果存入到 `MySQL` 数据库中



## 03-Django

- `path('', views.index)`                        采用图表方式展示舆情分析的结果
- `path('searchk/', views.searchk)`   在 `Web` 界面根据关键字或关键词进行搜索
- `path('searchd/', views.searchd)`   按照时间（录入时间）进行搜索



