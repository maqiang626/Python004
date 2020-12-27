# 毕业总结 (2020.12.21 - 2020.12.27)



[TOC]





------



# 版本更新历史

<table>
   <tr>
      <th align="center" width=59px>版本</th>
      <th>更新内容</th>
      <th>修订人</th>
      <th align="center" width=111px>更新时间</td>
   </tr>
   <tr>
      <td>v1.0</td>
      <td>毕业总结</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-12-27 21:00</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>









# 1. 课程内容知识点学习

## 1.1. Python 基础核心知识

- 爬虫相关
  - requests
  - BeautifulSoup bs4
  - XPath
  - 自动翻页

- 基础语法

- 前端知识

- Scrapy
  - 爬虫中间件
  - 系统代理 IP
  - 自定义中间件
  - 随机代理 IP
  - 并发参数优化

- 异常
- PyMySQL


- 反爬虫
  - fake-useragent

  - cookies

  - WebDriver

  - 验证码

- 分布式爬虫


- 多进程
  - 创建进程
  - 多进程调试
  - 使用队列实现进程间的通信
  - 管道共享内存
  - 锁机制解决资源抢占
  - 进程池

- 多线程
  - 创建线程
  - 队列
  - 线程池
  - GIL

- 数据清洗
  - pandas
  - 数据预处理
  - 数据调整
  - 基本操作
  - 分组聚合
  - 多表拼接
  - 输出和绘图
  - jieba 分词与提取关键词
  - SnowNLP 情感倾向



## 1.2. Python 高级进阶

- 类属性

- 对象属性

- 作用域

- 类方法

- 静态方法

- `__getattribute__`
- `__getattr__`

- 属性描述符 property

- 面向对象编程
  - 继承
  - SOLID
  - 单例模式
  - 工厂模式
- 元类
- mixin 模式

- 变量赋值

- 深浅拷贝

- collections

- 函数关注四个方面
  - 调用
  - 作用域
  - 参数
  - 返回值
- 闭包

- 装饰器

- 对象协议与鸭子类型

- 迭代器和生成器

- yield 语句

- yield 表达式

- 协程




## 1.3. Django 基础知识

- django-admin
- manage.py
- settings.py
- urls
- view
- ORM
- Models
- Template



## 1.4. Django 进阶

- 源码分析
  - URLconf 偏函数
  - URLconf include
  - view 请求
  - view 响应
  - view 完整流程
  - model 自增主键
  - model 查询管理器
  - template 加载文件
  - template 模板渲染

- 管理界面 admin

- 表单

- 表单 CSRF 防护

- 用户管理认证

- 信号

- 中间件

- 生产环境部署

- celery

- Flask

- Tornado






# 2. 期末作业

## 毕业项目

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
4. 数据展示支持按时间筛选和按关键词筛选功能（参考）
    [ https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817 ](https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817)

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



## 项目解析

解答链接：https://github.com/maqiang626/Python004/tree/master/Week13/graduation_project



## 项目解析说明

### 00-SQL

`PIP-requirements`  依赖包

- `requirements.txt`



`db_w13.sql`  数据库导出脚本文件

- `tb_original_comments`     原始评论相关信息
- `tb_semantic_emotion`       经过数据清洗和语义情感分析后的评论相关信息
- `tb_sentiment_analysis`   舆情分析结果



### 01-Scrapy

- 爬取“**什么值得买**”网站中“**笔记本电脑**”分类的“**24小时排行**”信息
- 爬取前 `10` 产品相关信息
- 爬取评论数量和分页相关信息
- 爬取具体评论相关信息
- 所有原始评论数据存入 `MySQL` 数据库



### 02-Pandas

- 从数据库中获取原始评论数据
- 对评论数据进行清洗
  - 去除重复值
  - 去除缺失值
- 对清洗后的数据进行语义情感分析
- `DataFrame` 数据（经过语义情感分析后的数据）存入数据库
- 舆情分析的结果存入到 `MySQL` 数据库中



### 03-Django

- `path('', views.index)`                        采用图表方式展示舆情分析的结果
- `path('searchk/', views.searchk)`   在 `Web` 界面根据关键字或关键词进行搜索
- `path('searchd/', views.searchd)`   按照时间（录入时间）进行搜索





# 3. 学习总结

## 3.1. 收获

1. 系统性的学习了 `Python` 相关知识
2. 系统性的学习了 `Django` 相关知识
3. 学习了一些其他相关知识



## 3.2. 问题及不足

1. 实践太少
2. 实际动手能力弱
3. 爬虫相关经验不足
4. `Django` 使用经验不足
5. `Python` 高阶知识欠缺



## 3.3. 改进

1. 继续深入 `Python` 相关知识学习
2. `Django` 相关知识深入学习和实践
3. 周边相关知识学习
4. 中间件知识



## 3.4. 感悟

​		2020 年最后的几个月，通过本课程系统性的学习了 Python，三个月的时间匆匆而过，总感觉自己学的远远不够，待到现在想总结一下的时候，才发现太多的不足。

​		感觉自己好像懂了，但深入又好像没太懂，究其原因有两个主要方面，一个是自己深入思考和总结的不够，另一个就还是动手太少，实践能力弱。

​		幸好现在还有更好的一个机会，2.0 版本已经来临，自己也会继续深入学习下去，期待能够真正把 Python 技术和能力夯实，加油！



