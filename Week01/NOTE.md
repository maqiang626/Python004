# Week01 学习笔记 (2020.9.21 - 2020.9.27)



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
      <td>1. 用 requests 写一个最简单的爬虫 <br>
          2. 使用 BeautifulSoup 解析爬取到的网页 <br>
          3. 使用 XPath 解析网页 <br>
          4. 实现爬虫的自动翻页功能 <br>
          5. Python基础语法回顾 <br>
          6. 前端基础：HTML基本结构 <br>
          7. 前端基础：HTTP协议 <br>
          8. Scrapy 框架结构解析 <br>
          9. Scrapy 爬虫目录结构解析 <br>
          10. 将 requests 爬虫改写为 Scrapy 爬虫 <br>
          11. 通过 Scrapy 爬虫爬取电影详情页信息 <br>
          12. XPath 详解 <br>
          13. yield 与推导式</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-09-27 21:50</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>







# 1. 课程内容知识点学习

## 1.1. 用 requests 写一个最简单的爬虫

### 1.1.1. 获取源代码

```powershell
git clone https://github.com/wilsonyin123/geekbangtrain.git
cd geekbangtrain
git checkout 1a
git switch 1a  # 同 git checkout 1a


# 使用 Gitee 代替 GitHub（内容一样）
git clone https://gitee.com/wilsonyin/pythontrain.git
cd pythontrain
git checkout 1a
```



### 1.1.2. 安装 **requests** 库（第三方库）

```powershell
pip install requests


# 使用临时 PIP 源（清华）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests


# 永久替换 PIP 源（清华）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



### 1.1.3. 源代码学习

**1a_requests.py**

> 1. 使用 requests 库的一个完整的爬取豆瓣电影的代码
> 2. user-agent：模拟浏览器登录
> 3. header：字典（HTTP 头部）
> 4. request.get：两个参数（url, headers）
> 5. response.text：爬取到的页面源代码完整内容
> 6. response.status_code：HTTP 返回码（200 ok）



**1a_urllib.py**

> 1. GET 方法
> 2. POST 方法
> 3. cookie（from http import cookiejar）



Python 内置库：**urllib**

```python
from urllib import request
```



### 1.1.4. requests 和 urllib 对比

> - requests 使用简单，同时应用广泛
> - requests 库官方文档清晰丰富，便于入手
> - urllib 首先导入较长 `from urllib import request`
> - urllib 使用略复杂，同时应用不普及



### 1.1.5. 开发流程四个步骤

> 1. 提出需求：功能点
> 2. 编码：完成功能
> 3. Run：代码 run 起来
> 4. 修复和完善：Bug



### 1.1.6. 本节总结

> 1. 开始入门爬虫的世界
> 2. 使用 `requests` 库轻松实现一个简单的爬虫
> 3. 使用 `requests` 库，如果去掉 `headers` 参数，运行则 `response.status_code = 418`
> 4. 使用内置库 urllib 使用复杂，而且不普及，了解即可
> 5. 期待后续更多爬虫的精彩



## 1.2. 使用 BeautifulSoup 解析爬取到的网页

### 1.2.1. 获取源代码

```powershell
git checkout 1b
```



### 1.2.2. 安装 **bs4** 库（第三方库）

```powershell
pip install bs4


# 使用临时 PIP 源（清华）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple bs4
```



### 1.2.3. 源代码学习

**1b_bs4.py**

> 1. 先使用 requests 库获取网页所有信息
> 2. 使用 BeautifulSoup 对获取的所有信息进行解析（html.parser）
> 3. 在浏览器上使用 `F12` 查看具体需要解析的内容所在的 `HTML` 标识
> 4. 针对具体的电影链接（href）和电影名称（'span'.text）进行循环获取（过滤条件）



### 1.2.4. 本节总结

> 1. 使用 BeautifulSoup 对 requests 爬取的网页信息进行解析
> 2. 需要了解 HTML 前端的知识，这样便于进行分析和获取



## 1.3. 使用 XPath 解析网页

### 1.3.1. 获取源代码

```powershell
git checkout 1c
```



### 1.3.2. 安装 **lxml pandas**（第三方库）

```powershell
pip install lxml
pip install pandas


# 使用临时 PIP 源（清华）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```



### 1.3.3. 源代码学习

**1c_movie.py**

> 1. 先使用 requests 库获取网页所有信息
> 2. 将获取的信息使用 `lxml` 处理 `lxml.etree.HTML(response.text)`
> 3. 在浏览器上使用 `F12` 查看具体需要解析的内容所在的 `HTML` 标识
> 4. F12 - Sources - (index) - 选中电影名称 - Elements 右键 - Copy - Copy XPath（后面加 `/text()`）
> 5. 电影名称、上映日期、评分，都采取上面同样的操作方式，经过 `xml` 处理后，结果组成列表
> 6. 使用 pandas 将列表数据保存为 csv 格式的文件 `encoding='utf8'`



### 1.3.4. 本节总结

> 1. 使用 BeautifulSoup 和 XPath 都可以对获取的网页信息进行解析
> 2. 使用 XPath 解析更高效（C 语言编写），同时也更简单
> 3. XPath 路径解析的具体写法需要细化和掌握
> 4. XPath 调试方法（浏览器 `F12` 模式）
> 5. 使用 pandas 保存文件时，Linux 支持 utf8 编码，Windows 支持 gbk 编码



## 1.4. 实现爬虫的自动翻页功能

### 1.4.1. 获取源代码

```powershell
git checkout 1c
```



### 1.4.2. 源代码学习

**1c_PageTurn.py**

> 1. 将获取电影链接和电影名称封装为一个函数，参数为页面 URL `get_url_name(myurl)`
> 2. 在浏览器上使用 F12 查看具体需要解析的内容所在的 `HTML` 标识
> 3. 在方法里面使用 requests 库获取网页所有信息，并使用 BeautifulSoup 进行循环解析
> 4. 所有的页面 URL 使用推导式生成元组 `tuple()`
> 5. 循环传参进行自动翻页功能
> 6. 使用 Python 内置模块 `time` 进行 `sleep` 操作



### 1.4.3. 本节总结

> 1. 必要时封装函数操作更高效
> 2. 推导式生成元组需要 `tuple` 前缀
> 3. 控制爬取频率以防反爬 `sleep(5)`
> 4. 通过丰富的第三方库和 `Python` 的基础语法，完成静态页面的读取



## 1.5. Python基础语法回顾

### 1.5.1. 获取源代码

```powershell
git checkout 1c
```



### 1.5.2. 源代码学习

**1c_python.py**

> 1. 便捷交换变量 `var2, var1 = var1, var2`
> 2. 所有语言的开头 `print('Hello World')`
> 3. 可交互字节码 `help() / dir() / exit()`
> 4. 内置数据类型 `数值 / 布尔 / 字符串 / 列表 / 元组 / 字典 / 集合`
> 5. 流程控制 `if / elif /else / for in / while / break / continue`
> 6. 函数 `def / return`
> 7. 面向对象 `class / def / self / __init__`
> 8. 标准库 `datetime`



### 1.5.3. 本节总结

> 1. 基础不牢地动山摇
> 2. 官方文档（相应版本）
> 3. 实践出真知
> 4. `type` 用作变量名不会报错，但是 `type` 本身是 `Python` 关键字



## 1.6. 前端基础：HTML基本结构

**W3C 标准官方文档：**https://www.w3.org/standards/



### 1.6.1. 知识学习

> 1. HTML 常用属性和标签 `html / head / body / div / class / a / span / href / img`
> 2. HTML `css / javascript / json`
> 3. 浏览器 `Chrome / Firefox / Safari`



### 1.6.2. 本节总结

> 1. 掌握 **HTML** 基础和高阶知识
> 2. **CSS / JavaScript**
> 3. 浏览器 **F12** 分析调试



## 1.7. 前端基础：HTTP协议

### 1.7.1. 知识学习

> 1. HTTP 请求和返回头部 `Headers`
> 2. 请求方式 `get / post / delete / head / put`
> 3. 状态码 `1** / 200 / 2** / 302 / 3** / 403 / 404 / 418 / 4** / 500 / 5**`
> 4. 客户端请求和服务器响应



### 1.7.2. 本节总结

> 1. 网络知识加固
> 2. 三次握手四次挥手
> 3. TCP/IP 四元组
> 4. OSI 七层和TCP/IP 四层



## 1.8. Scrapy 框架结构解析

Scrapy 架构官方文档介绍：[ https://docs.scrapy.org/en/latest/topics/architecture.html ](https://docs.scrapy.org/en/latest/topics/architecture.html)



### 1.8.1. 知识学习

> 1. Scrapy 核心组件
>    - Engine (引擎)
>    - Scheduler (调度器)
>    - Downloader (下载器)
>    - Downloader Middlewares (下载器中间件)
>    - ### Spider Middlewares (爬虫中间件)
>    - Spider (爬虫)
>    - Item Pipelines (项目管道) 
> 2. 需要修改 `Spider (爬虫) / Item Pipelines (项目管道)` 



### 1.8.2. 本节总结

> 1. Data flow (1-8) / The process repeats (from step 1) until there are no more requests from the
>    Scheduler
> 2. 反复理解框架流程和处理逻辑



## 1.9. Scrapy 爬虫目录结构解析

### 1.9.1. 获取源代码

```powershell
git checkout 2a
```



### 1.9.2. 安装 **scrapy**（第三方库）

```powershell
pip install scrapy


# 使用临时 PIP 源（清华）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy
```



### 1.9.3. Scrapy 使用步骤

```powershell
# Creating a project
scrapy startproject doubanmovie
cd ./doubanmovie/doubanmovie/spiders
scrapy genspider douban movie.douban.com
```



### 1.9.4. 源代码学习

初始化创建项目，源代码目录结构：

> **.\DOUBANMOVIE**
> │  scrapy.cfg
> │
> └─doubanmovie
>     │  items.py
>     │  middlewares.py
>     │  pipelines.py
>     │  settings.py
>     │  `__init__.py`
>     │
>     ├─spiders
>     │  │  douban.py
>     │  │  `__init__.py`
>     │  │
>     │  └─`__pycache__`
>     │          `__init__.cpython-37.pyc`
>     │
>     └─`__pycache__`
>             settings.cpython-37.pyc
>             `__init__.cpython-37.pyc`



**scrapy.cfg**

> 1. 项目的配置文件
> 2. 创建项目后，此文件目前一般保持不变

- [x] **items.py**

> 1. 定义所爬取记录的数据结构
> 2. 此文件需要根据需求进行修改
> 3. 定义变量 `title / link`
> 4. 变量值固定保持不变 `scrapy.Field()`

**middlewares.py**

> 1. 中间件文件
> 2. 创建项目后，此文件目前一般保持不变

- [x] **pipelines.py**

> 1. 设置保持位置
> 2. 此文件需要根据需求进行修改
> 3. 根据 item 可以在此文件定义是否要打印输出、或输出到指定文件、或保存到数据库
> 4. 结尾需返回 item `return item`

- [x] **settings.py**

> 1. 项目的配置文件
> 2. 此文件需要根据需求进行修改
> 3. 模拟浏览器访问 `USER_AGENT`
> 4. 防止反爬 `DOWNLOAD_DELAY = 3`
> 5. 当爬取结果输出到文件时，需要开启设置 `ITEM_PIPELINES`

**spiders**`（目录）`

> 1. Scrapy 创建项目时固定生成的目录，不可更改
> 2. 里面包含实现爬虫的具体文件和 `__init__.py` 文件

- [x] **spiders\douban.py**

> 1. 实现爬虫的文件，编写具体的爬虫逻辑
> 2. 初始类定义 `DoubanSpider(scrapy.Spider)`
> 3. 三个变量含义和原理 `name / allowed_domains / start_urls`
> 4. 爬虫启动时引擎调用的方法 `start_requests(self)`
> 5. 回调函数调用具体的解析方法 `parse(self, response)`
> 6. 具体的解析函数返回给 pipelines 进行后续的文件处理 `return items`



### 1.9.5. 本节总结

> 1. 结合 Scrapy 框架剖析 Scrapy 具体的目录结构
> 2. 所有文件都是 Python 文件，包括相应的配置文件和设置文件，修改均需遵从 Python 语法
> 3. 区分不可更改的文件和目录，以及需要修改的文件



## 1.10. 将 requests 爬虫改写为 Scrapy 爬虫

### 1.10.1. 获取源代码

```powershell
git checkout 2b
```



### 1.10.2. 源代码学习

保持不变：

> 1. 源代码目录结构保持不变
> 2. 具体代码文件不变 `scrapy.cfg` `__init__.py` `items.py` `middlewares.py`

**pipelines.py**

> 1. 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
> 2. 将 item 信息输出到文件 `doubanmovie.txt` `process_item(self, item, spider)`

**settings.py**

> 1. 针对 USER_AGENT 使用 USER_AGENT_LIST `USER_AGENT = random.choice(USER_AGENT_LIST)`
>
> 2. 开启 `ITEM_PIPELINES`
>
>    ```python
>    ITEM_PIPELINES = {
>        'doubanmovie.pipelines.DoubanmoviePipeline': 300,
>    }
>    ```
>
>    

**douban.py**

> 1. 针对 BeautifulSoup 获取的电影页面信息进行解析
>
>    ```python
>    for i in title_list
>    ```
>
> 2. 回调 `yield scrapy.Request(url=url, callback=self.parse)`



### 1.10.3. 本节总结

> 1. 充分发挥 `Scrapy` 优势
> 2. 目录结构内的文件环环相扣
> 3. `Scrapy`解耦，增加可维护性
> 4. 列出爬虫 `scrapy list`
> 5. 运行爬虫 `scrapy crawl douban`



## 1.11. 通过 Scrapy 爬虫爬取电影详情页信息

### 1.11.1. 获取源代码

```powershell
git checkout 2b
```



### 1.11.2. 源代码学习

**items.py**

> 1. 爬取内容增加电源简介，相应的需要在 `items` 里面增加条目
> 2. 增加变量 `content = scrapy.Field()`

**douban.py**

> 1. 在 `parse` 中回调函数执行 `parse2`
>
>    ```python
>    yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
>    ```
>
> 2. 在 `parse2` 中接收 `item = response.meta['item']` ，解析具体页面获取电影简介并返回 `yield item`



### 1.11.3. 本节总结

> 1. `callback` 回调函数需处理
> 2. 复杂业务处理



## 1.12. XPath 详解

### 1.12.1 获取源代码

```powershell
git checkout 2c
```



### 1.12.2. 源代码学习

**douban.py**

> 1. 使用 Scrapy 自带的 selector `from scrapy.selector import Selector`
>
> 2. 过滤重复 URL `dont_filter=False`
>
> 3. 使用 XPath 过滤页面内容 `Selector(response=response).xpath('//div[@class="hd"]')`
>
> 4. 内容和属性采用不同形式获取
>
>    ```python
>    title = movie.xpath('./a/span/text()')
>    link = movie.xpath('./a/@href')
>    
>    title = movie.xpath('./a/span/text()').extract_first().strip()
>    link = movie.xpath('./a/@href').extract_first().strip()
>    ```



### 1.12.3. 本节总结

> 1. XPath -> xml `lxml`
> 2. XPath 路径匹配符号区别 `//  /  ./  ../`
> 3. XPath 效率远高于 BeautifulSoup
>    - BeautifulSoup：纯 Python 实现；全局查找
>    - XPath：C 语言实现；相对路径匹配
> 4. 学习不同路径不同情况下的 XPath 匹配方式



## 1.13. yield 与推导式

### 1.13.1. 获取源代码

```powershell
git checkout 2d
```



### 1.13.2. 源代码学习

**comprehension.py**

> 1. 列表推导式：便捷操作
> 2. 嵌套循环：双重 `for` 循环 `[str(i) + j for i in range(1, 6) for j in 'ABCDE']`
> 3. 用推导式将字典转换为列表 `mydict.items()`
> 4. 推导式生成字典 `{}`
> 5. 推导式实现字典的k-v互换 `{value: key for key, value in mydict.items()}`
> 6. 推导式生成集合：`for / if`
> 7. 推导式生成生成器 `<generator object <genexpr> at 0x0000010DE57A3748>`

**yield_demo.py**

> 1. `yield` 返回值
> 2. next 获取返回值



### 1.13.3. 本节总结

> 1. 推导式生成元组需要 `tuple` 前缀
> 2. `yield` 可以作为语句和表达式来使用
> 3. `yield / return` 区别





# 2. 本周作业

## 2.1. 作业一

### 2.1.1. 作业说明

> 安装并使用 requests、bs4 库，爬取[猫眼电影](https://maoyan.com/films?showType=3)的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
>
> **猫眼电影网址：**[ https://maoyan.com/films?showType=3 ](https://maoyan.com/films?showType=3)



### 2.1.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week01/job1



实现过程：

> 1. 使用 requests 获取猫眼电影页面内容
> 2. 使用 bs4 BeautifulSoup 对获取的页面内容进行 html 解析
> 3. 针对解析的内容循环获取前 10 个电影名称、电影类型和上映时间
> 4. 使用 pandas 将获取的电影信息保存到 csv 格式的文件中



代码说明：

> 1. headers 获取：页面 F12 指定 `user-agent` / `Cookie`（可选 / 反爬）
> 2. movie_info 字典汇总信息：`value` 为 `list` 类型（增加序号和标题）
> 3. movie_data 汇总每个电影的所有信息
> 4. divs 汇总每个电影的具体条目信息
> 5. 针对 divs 分别获取电影名称、电影类型和上映时间
> 6. pandas：encoding (Linux: utf8 / Windows: gbk)
> 7. 定义方法：get_movie_info(url)



问题及解决方案：

> - [x] DEBUG: Redirecting (302) to <GET https://sec.douban.com/b?r=https%3A%2F%2Fmovie.douban.com%2Frobots.txt> from <GET https://movie.douban.com/robots.txt>
>   - 浏览器 `F12` 调试，获取 `Cookie`
>   - 代码中 `headers` 增加 `Cookie`
> - [x] 爬取前 10 个电影信息
>   - `BeautifulSoup` 查找 `find_all` 方法增加参数 `limit=10`
> - [x] 获取每个电影的所有信息
>   - 各种方法综合运用 `find_all / find / text / split()[1] / strip()`



## 2.2. 作业二

### 2.2.1. 作业说明

> 使用 Scrapy 框架和 XPath 抓取[猫眼电影](https://maoyan.com/films?showType=3)的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
>
> **猫眼电影网址：**[ https://maoyan.com/films?showType=3 ](https://maoyan.com/films?showType=3)
>
> **要求：**必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。



### 2.2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week01/job2



实现过程：

> 1. 使用 scrapy 创建项目和爬虫
> 2. 创建需要爬取的对应条目：电影名称、电影类型和上映时间
> 3. 使用 scrapy.selector 获取指定 URL 页面内容
> 4. 使用 XPath 对获取的页面内容进行解析
> 5. 针对解析的内容循环获取前 10 个电影名称、电影类型和上映时间
> 6. 使用 with 上下文管理器将获取的电影信息保存到 csv 格式的文件中



代码说明：

> 1. items：增加条目：电影名称、电影类型和上映时间
>
> 2. pipelines：直接使用 with 上下文管理器保存 item 信息
>
> 3. settings：USER_AGENT / DOWNLOAD_DELAY / ITEM_PIPELINES
>
>    ```python
>    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
>    
>    DOWNLOAD_DELAY = 3
>    
>    ITEM_PIPELINES = {
>       'maoyanmovie.pipelines.MaoyanmoviePipeline': 300,
>    }
>    ```
>
> 4. maoyan：scrapy.Request(url=url, callback=self.parse, dont_filter=False) / items.append(item) / return items



问题及解决方案：

> - [x] 出现输出 <div class='logo' id='logo'>验证中心</div>
>   - 打开验证页面，手动滑动滑块，手动验证通过
> - [x] 获取每个电影的所有信息
>   - 各种方法综合运用 `span / text() / divs[0] / get() / getall()[1] / strip()`





# 3. 学习总结

## 3.1. 收获

1. 使用 requests 便捷使用一个爬虫，爬取指定链接的静态页面信息
2. 使用 BeautifulSoup 对爬取的页面进行内容解析
3. 使用 XPath 更高效的进行页面内容解析
4. 掌握了自动翻页功能的实现
5. 回顾了 Python 基础语法
6. 了解了 HTTP 前端知识和协议相关知识
7. 对 Scrapy 框架和基本原理有了初步的了解，并结合代码结构进行了一一匹配
8. 通过 Scrapy 改写了 requests 爬虫，并结合 XPath 解析，进一步加深了 Scrapy 爬虫知识
9. 学习了推导式和 yield 相关知识



## 3.2. 不足

1. 针对 BeautifulSoup 解析页面内容时，相应的方法不熟悉
2. 针对 XPath 解析页面内容时，过滤规则和方法不熟悉
3. Python 基础知识掌握的还不够精通
4. HTTP 相关知识不够精通
5. Scrapy 博大精深，还需深入学习和掌握
6. 推导式和 yield 实战还需加强



## 3.3. 改进

### 3.3.1. 深入学习

1. 更多的总结和学习 BeautifulSoup 和 XPath 的相关知识
2. Python 基础知识加固
3. HTTP 相关知识加固
4. Scrapy 深入学习
5. 推导式相关知识和 yield 相关知识深入学习



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

​        Python 主讲老师，尹会生老师，讲课认真细致，一丝不苟，之前还学过他出品的《零基础学 Python》和《Linux实战技能100讲》，技艺精湛，水平高超，学下来受益匪浅，这次能有幸参加 Python 进阶训练营，首先心里已经特别开心，其次通过这一周的学习，对 Python 有了更大的兴趣，接下来更要认认真真把整个训练营拿下。

​        助教老师，王佳兴老师，真的特别佩服，自从他加到我们微信讨论群以来，知无不言言无不尽，经常见他毫不疲倦的回答各种问题，由浅入深，我自己也通过群里面各种问题和他的解答中学习到了很多，为我们这期训练营有一个这么好的助教点赞。

​        班班，鱼丸，Amy，自从报名以来，无论大小问题，有求必应，从不拖沓；而且上次和她说还打算参加算法训练营，班班说能给老学员申请更优惠的资格，棒棒哒。

​        自己呢，本身有一定的 Python 基础，但是也由于工作中使用较少，实战较少，所以没有太多实战经验。通过这次训练营，自己跟着学习，并且全部自己动手，仅仅一周的时间，已经感觉和 Python 有一种相见恨晚的感觉，所以在接下来的时间里，一定要时刻告诉自己，勤勉，努力，多学，多练；加油！

​        星光不问赶路人，在漫漫前行的道路上，可能恰好就像第一课爬取的《豆瓣电影 Top 250》 的第一部电影一样，《肖申克的救赎》，我觉得我们每个人也都需要自我救赎，如果你不自救，可能真的就连上帝也救不了你；惟愿时光不负有心人，在这 2020 仅剩的时光里，用力播撒希望的种子，我亦能乘风破浪，愈挫愈勇，踏破黑暗，走向光明，一往无前！

