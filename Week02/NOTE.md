# Week02 学习笔记 (2020.9.28 - 2020.10.11)



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
      <td>1. 异常捕获与处理 <br>
          2. 使用 PyMySQL 进行数据库操作 <br>
          3. 反爬虫：模拟浏览器的头部信息 <br>
          4. 反爬虫：cookies 验证 <br>
          5. 反爬虫：使用 WebDriver 模拟浏览器行为 <br>
          6. 反爬虫：验证码识别 <br>
          7. 爬虫中间件 & 系统代理 IP <br>
          8. 自定义中间件 & 随机代理 IP <br>
          9. 分布式爬虫</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-10-11 18:28</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>









# 1. 课程内容知识点学习

## 1.1. 异常捕获与处理

### 1.1.1. 获取源代码

```powershell
git checkout 2d
```



### 1.1.2. 安装 **pretty_errors** 库（第三方库）

```powershell
pip install pretty_errors
```



### 1.1.3. 源代码学习

**2d\exception_demo.py**

> 1. 注意异常三个关注点
> 2. 第一个关注点：Traceback (most recent call last):
> 3. 第二个关注点：哪一个文件的第几行
> 4. 第三个关注点：ZeroDivisionError: division by zero
> 5. 异常捕获



**2d\exception_demo\p1_dive0.py**

> 1. ZeroDivisionError: division by zero
> 2. 发生异常后面的程序不再执行 -> 所以必须进行异常处理，不中断业务



**2d\exception_demo\p2_try.py**

> 1. try / except / 嵌套捕获异常 (代码缩进进行区分) / 多重异常处理
> 2. 异常捕获输出 `division by zero`



**2d\exception_demo\p3_chain.py**

> 1. list index out of range
> 2. 捕获到异常后，后面的异常不再捕获
> 3. 清晰了解整个程序的运行过程，多调试输出



**2d\exception_demo\p4_inputerror.py**

> 1. 自定义异常 UserInputError (class UserInputError(Exception):)
> 2. 自定义类，继承自 Exception
>    - `__init__(self, ErrorInfo):`
>      - ErrorInfo 错误信息返回 (固定写法)
>    - `__str__(self):`
>      - 魔术方法
>      - 类像字符串一样使用：可以打印输出
> 3. 使用 raise 抛出异常；后续对抛出的异常进行相应的处理
> 4. raise UserInputError('用户输入错误')
> 5. try / except / finally
> 6. 释放变量占用的内存 `del userinput`



**2d\exception_demo\p5_pretty.py**

> 1. `import pretty_errors`
>
> 2. 美化异常输出
>
>    ```python
>    # ========================== MQDEBUG INFO ==========================
>    # p5_pretty.py 5 <module>
>    # foo()
>    # 
>    # p5_pretty.py 3 foo
>    # 1/0
>    # 
>    # ZeroDivisionError:
>    # division by zero
>    
>    ```



**2d\exception_demo\p6_with.py**

> 1. 使用 with 对文件操作
> 2. with open('a.txt', encoding='utf8') as file2:
> 3. 使用 with 上下文管理器简化操作 `Pythonic`



**2d\exception_demo\p7_custom_with.py**

> 1. 自定义 `Open() / __enter__ / __exit__ / __call__`
> 2. 上下文协议 `with Open() as f:`
> 3. `__call__` 将类当做函数使用
> 4. 魔术方法：各种常见的魔术方法和功能



### 1.1.4. 异常捕获过程

> 1. 异常类把错误消息打包到一个对象
> 2. 该对象会自动查找到调用栈
> 3. 直到运行系统找到明确声明如何处理这些类异常的位置



### 1.1.5. 本节总结

> 1. 异常并不完全等于错误，错误范围更大
> 2. 异常也是一个类，所有异常继承自 `BaseException`
> 3. 异常：用户异常输入 / 代码中异常
> 4. 代码健壮的标准：异常捕获与处理
> 5. 今后自己书写的代码中必须谨记进行异常捕获与处理
> 6. 捕获 = 陷阱
> 7. 使用 `pretty_errors` 更美化异常捕获
> 8. 学会自定义异常捕获类
> 9. 另类思路：学会如何产生异常 / 生成器
> 10. 异常类型：各种异常类型模拟和处理
>    - LookupError / IndexError / KeyError
>    - IOError
>    - NameError: name 'browser' is not defined
>    - TypeError
>    - AttributeError
>    - ZeroDivisionError: division by zero
>    - FileNotFoundError: [Errno 2] No such file or directory: 'cap.jpg'
>    - FileNotFoundError: [WinError 2] 系统找不到指定的文件
>    - ModuleNotFoundError: No module named 'pymysql'
>    - StopIteration (yield)



## 1.2. 使用 PyMySQL 进行数据库操作

### 1.2.1. 获取源代码

```powershell
git checkout 2d
```



### 1.2.2. 安装 **pymysql** 库（第三方库）

```powershell
pip install pymysql
```



### 1.2.3. 源代码学习

**2d\pymysql\p1_pymysql.py**

> 1. 定义数据库相关信息 `host / port / user / passwd / db`
> 2. 根据一般流程进行操作
> 3. SQL 语句 (书写规范)
>    - SELECT 1
>    - SELECT VERSION()
> 4. try / catch /finally
> 5. 游标建立的时候就开启了一个隐形的事务
> 6. conn.commit() / conn.rollback() / conn.close()
> 7. 类实例化 / 调用方法执行
> 8. 返回元组组成的列表信息 `[(1,), ('5.6.27-log',)]`



**2d\pymysql\p2_select.py**

> 1. charset = 'utf8mb4' / utf8 / utf-8 (区别) (!@@)
> 2. CRUD 日常操作
> 3. 第一条 fetchone() / 所有数据 fetchall() /返回值和类型 (!@@)
> 4. 批量操作 executemany()
> 5. 最后养成好习惯：关闭游标，关闭连接



### 1.2.4. 一般流程

> 1. 创建连接 `pymysql.connect()`
> 2. 创建游标 `conn.cursor()`
> 3. 执行 SQL 语句 CRUD `cursor.execute(sql)`
> 4. 关闭游标 `cursor.close()`
> 5. 关闭连接 `conn.close()`



### 1.2.5. 本节总结

> 1. MySQL 安装和初始化配置 (Windows / Linux / Mac)
> 2. 检查 MySQL 启动状态 `ps -ef | grep mysql`
> 3. MySQL 登录 `mysql -uroot -p******`
> 4. MySQL 配置不建议写到代码中
>    - 代码中不方便修改
>    - 代码开源共享后会泄露信息
>    - 建议通过配置文件进行加载
>    - 自定义 `settings.py`
> 5. pymysql
>    - 第三方库官方文档
>    - 纯 Python 实现：Ctrl + 点击方法；追踪定义；一直回溯定义
>    - 使用 pymysql 轻松实现 Python 对 MySQL 数据库的 CRUD 操作
>    - 更稳定 / 类比 mysql-connector （MySQL 官方提供的驱动器）
> 6. 后面学习重点：ORM 框架 SQLAIchemy
> 7. 数据库 CRUD 需熟练
> 8. 数据库不使用的时候及时断开，释放资源
> 9. 尽量复用已有的连接进行日常操作
> 10. Python 对传入的参数当作对象处理 (自己关注传入参数的类型) `Type Hint`



## 1.3. 反爬虫：模拟浏览器的头部信息

### 1.3.1. 获取源代码

```powershell
git checkout 2e
```



### 1.3.2. 安装 **fake-useragent**（第三方库）

```powershell
pip install fake-useragent
```



### 1.3.3. 源代码学习

**2e\p1_useragent.py**

> 1. from fake_useragent import UserAgent
>
> 2. 不验证 SSL `verify_ssl=False`
>
> 3. 可方便模拟不同的浏览器 `User-Agent`
>
>    ```python
>    print(f'Chrome浏览器: {ua.chrome}')
>    print(ua.safari)
>    print(ua.ie)
>    print(f'随机浏览器: {ua.random}')
>    
>    
>    # ========================== MQDEBUG INFO ==========================
>    # Chrome浏览器: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36
>    # Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27
>    # Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8
>    # 随机浏览器: Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36
>    
>    ```



### 1.3.4. 本节总结

> 1. `fake_useragent` 见名知意
> 2. 使用 `fake_useragent` 方便模拟浏览器头部信息
> 3. 使用随机选择更高效；通过头部信息解决反爬虫
> 4. 话题：反爬虫和反反爬虫
> 5. 反反爬虫：让你的行为更像浏览器
> 6. 爬虫判断：根据基本请求判断 / 根据行为进行判断
> 7. 头部信息三个：`User-Agent / Host / Referer`
> 8. 常用浏览器
>    - Chrome
>    - Firefox
>    - Safari
>    - IE
>    - Microsoft Edge
>    - 安卓手机浏览器
>    - 苹果手机浏览器



## 1.4. 反爬虫：cookies 验证

### 1.4.1. 获取源代码

```powershell
git checkout 2e
```



### 1.4.2. 源代码学习

**2e\p2_GetandPost.py**

> 1. import requests
> 2. requests.get() `status_code / headers['content-type'] / text / encoding / json()`
> 3. requests.post() `data 参数 / 返回：json()`
>    - Request Method: GET
>    - Statis Code: 405 METHOD NOT ALLOWED
> 4. 使用 httpbin 网站方便进行调试和学习



**2e\p3_cookies.py**

> 1. s = requests.Session() (CTRL 跟踪)
> 2. 'http://httpbin.org/cookies/set/sessioncookie/123456789'
> 3. 在同一个 Session 实例发出的所有请求之间保存 cookie
> 4. 会话使用上下文管理器 `with requests.Session() as s:`



**2e\p4_cookie_requests.py**

> 1. 使用 fake_useragent 模拟浏览器头部信息
> 2. headers 增加 Referer 参数信息：防止跨站
> 3. post 数据前获取 cookie / data
>    - login_url: Request URL
>    - form_data: 提交完整 (**需要和浏览器完全一致**)
> 4. 登陆后可以进行后续的请求 `requests.Session().get()`
> 5. 关注点 F12
>    - Request URL
>    - Request Method: POST
>      - Scrapy: Start_urls
>    - Host
>    - Referer: 从哪里跳转过来的



### 1.4.3. 本节总结

> 1. http://www.httpbin.org/ 方便的 HTTP 调试的网站
> 2. `Shift + Enter` 交互模式下调试 `Python` 程序
> 3. 直接复制 F12 展示的 Cookie 信息
>    - 保存用户名和密码
>    - Cookie 有效期 `expiry`
> 4. 模拟用户登录 POST



## 1.5. 反爬虫：使用 WebDriver 模拟浏览器行为

### 1.5.1. 获取源代码

```powershell
git checkout 2e
```



### 1.5.2. 安装 **selenium**（第三方库）

```powershell
pip install selenium


# 安装 chromedriver
# http://chromedriver.storage.googleapis.com/index.html
#
# 2020-09-30 13:19
# Google Chrome 已是最新版本
# 版本 85.0.4183.121（正式版本） （64 位）
# http://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/
# chromedriver_win32.zip (5,204,275 Bytes)

```



### 1.5.3. 源代码学习

**2e\p5_cookie_webdriver.py**

> 1. 导入 webdriver `from selenium import webdriver`
> 2. 唤起浏览器 `browser = webdriver.Chrome()`
> 3. browser 方法 
>    - get()
>    - switch_to_frame()
>    - find_element_by_xpath() / send_keys()
>    - find_element_by_id() / click()
>    - get_cookies()
> 4. 'expiry': 1632981170



**2e\p6_short.py**

> 1. webdriver.Chrome()
> 2. 直接点击按钮 `browser.find_element_by_xpath()`
> 3. browser.page_source
> 4. try / except / finally



**2e\p7_filedownload.py**

> 1. 使用 `requests` 进行请求 `requests.get(url)`
> 2. 小文件下载直接使用 `with` 即可，采用 `wb` 方式写入
> 3. 大文件下载分块写入
>    - stream=True         # 流式数据
>    - wb                           # 二进制
>    - chunk_size=1024  # 分块数据大小
>    - if chunk:                 # 如果还有数据，就继续写入



### 1.5.4. 本节总结

> 1. webdriver 和 Chrome 之间的驱动：chromedriver_win32.zip / chromedriver.exe
> 2. 将 Chrome 对应版本的 chromedriver.exe 放到 venv 目录并添加环境变量 `Path`
> 3. Chrome  默认安装路径 `C:\Program Files\Google\Chrome\Application`
>    - 添加环境变量 `Path`
> 4. 报错 `NameError: name 'browser' is not defined`
>    - 将 chromedriver.exe 放到安装目录
>    - 添加 Path `C:\Program Files\Google\Chrome\Application`
>    - 重启 VSCode
> 5. selenium 博大精深，需深入研究



## 1.6. 反爬虫：验证码识别

### 1.6.1. 获取源代码

```powershell
git checkout 2e
```



### 1.6.2. 安装 **pillow pytesseract**（第三方库）

```powershell
pip install pillow
pip install pytesseract
```



### 1.6.3. 源代码学习

**2e\p8_captcha\验证码识别\captcha_pil.py**

> 1. 先使用 requests 下载验证码图片到本地
> 2. Image 打开图片 -> 观察图片，分析解决方法
> 3. 灰度图片 `convert('L')` -> 保存图片 -> 关闭图片流
> 4. 二值化 `threshold` -> 重新保存图片
> 5. 使用 pytesseract 将图片切分，识别为字符
>    - 默认支持语言 `chi_sim+eng`
>    - 各种语言识别库 https://github.com/tesseract-ocr/tessdata



### 1.6.4. 本节总结

> 1. MAC / Linux 安装 `brew install leptonica / brew install tesseract`
>    - Windows 对应安装？(!@@)
> 2. C++: OpenCV
> 3. 图片识别码正确识别之后，后续填入到指定的地方进行后续爬虫处理



## 1.7. 爬虫中间件 & 系统代理 IP

### 1.7.1. 获取源代码

```powershell
git checkout 3a
```



### 1.7.2. 源代码学习

针对 proxyspider，不变的默认 scrapy 代码

- 3a\proxyspider\scrapy.cfg
- `3a\proxyspider\proxyspider\__init__.py`
- 3a\proxyspider\proxyspider\items.py
- 3a\proxyspider\proxyspider\middlewares.py
- 3a\proxyspider\proxyspider\pipelines.py
- `3a\proxyspider\proxyspider\spiders\__init__.py`



**3a\proxyspider\proxyspider\middlewares.py**

针对 `ProxyspiderDownloaderMiddleware` 类

- from_crawler(cls, crawler)
- process_request(self, request, spider)
- process_response(self, request, response, spider)
- process_exception(self, request, exception, spider)
- spider_opened(self, spider)



**3a\proxyspider\proxyspider\settings.py**

> 开启下载中间件 `DownloaderMiddlewares`
>
> ```python
> DOWNLOADER_MIDDLEWARES = {
>     'proxyspider.middlewares.ProxyspiderDownloaderMiddleware': 543,
>     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
>     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
> }
> ```



**3a\proxyspider\proxyspider\spiders\httpbin.py**

> 1. name = 'httpbin'
> 2. 增加环境变量 `export http_proxy='http://52.179.231.206:80'`
> 3. 使用 httpbin 获取系统代理 IP `start_urls = ['http://httpbin.org/ip']`
> 4. 通过 Request.meta['proxy'] 读取 `http_proxy` 环境变量加载代理
> 5. 使用 response 直接返回信息 `print(response.text)`
> 6. 中间过程可以进行调试
>    -  通过 `headers` 查看 `user-agent` 
>      - `start_urls = ['http://httpbin.org/headers']`





### 1.7.3 Scrapy Data flow

The data flow in Scrapy is controlled by the execution engine, and goes like this:

1. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) gets the initial Requests to crawl from the [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders).
2. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) schedules the Requests in the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for the next Requests to crawl.
3. The [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) returns the next Requests to the [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine).
4. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) sends the Requests to the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader), passing through the [Downloader Middlewares](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_request()`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_request)).
5. Once the page finishes downloading the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader) generates a Response (with that page) and sends it to the Engine, passing through the [Downloader Middlewares](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader-middleware) (see [`process_response()`](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#scrapy.downloadermiddlewares.DownloaderMiddleware.process_response)).
6. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) receives the Response from the [Downloader](https://docs.scrapy.org/en/latest/topics/architecture.html#component-downloader) and sends it to the [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders) for processing, passing through the [Spider Middleware](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_input()`](https://docs.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_input)).
7. The [Spider](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spiders) processes the Response and returns scraped items and new Requests (to follow) to the [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine), passing through the [Spider Middleware](https://docs.scrapy.org/en/latest/topics/architecture.html#component-spider-middleware) (see [`process_spider_output()`](https://docs.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output)).
8. The [Engine](https://docs.scrapy.org/en/latest/topics/architecture.html#component-engine) sends processed items to [Item Pipelines](https://docs.scrapy.org/en/latest/topics/architecture.html#component-pipelines), then send processed Requests to the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler) and asks for possible next Requests to crawl.
9. The process repeats (from step 1) until there are no more requests from the [Scheduler](https://docs.scrapy.org/en/latest/topics/architecture.html#component-scheduler).



### 1.7.4. 本节总结

> 1. Scrapy 中间件有两类：下载中间件 `DownloaderMiddlewares` 和 爬虫中间件 `SpiderMiddlewares`
> 2. 爬虫中间件使用较少；下载中间件使用较多
> 3. 设置环境变量 `http_proxy = http://91.205.174.26:80`
>    - 重启 cmd
>    - 重启 VSCode
> 4. 若出现下面错误，则是代理 IP 问题，更换代理 IP 即可
>    - [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
>    - [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://httpbin.org/robots.txt> (failed 1 times): TCP connection timed out: 10060: 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
>    - [scrapy.downloadermiddlewares.retry] ERROR: Gave up retrying <GET http://httpbin.org/ip> (failed 2 times): TCP connection timed out: 10060: 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
>    - [scrapy.downloadermiddlewares.retry] ERROR: Gave up retrying <GET http://httpbin.org/ip> (failed 3 times): TCP connection timed out: 10060: 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
>    - 'retry/reason_count/twisted.internet.error.TCPTimedOutError': 4



## 1.8. 自定义中间件 & 随机代理 IP

### 1.8.1. 获取源代码

```powershell
git checkout 3a
```



### 1.8.2. 源代码学习

针对 randproxy，不变的默认 scrapy 代码

- 3a\randproxy\scrapy.cfg
- `3a\randproxy\proxyspider\__init__.py`
- 3a\randproxy\proxyspider\items.py
- 3a\randproxy\proxyspider\pipelines.py
- `3a\proxyspider\proxyspider\spiders\__init__.py`



**3a\randproxy\proxyspider\middlewares.py**

> 1. 增加自定义类 `RandomHttpProxyMiddleware(HttpProxyMiddleware)`，继承自官方类 `HttpProxyMiddleware`
> 2. 重写三个方法 `__init__ / from_crawler / _set_proxy`
> 3. 初始化方法 `__init__`
>    - 从 `from_crawler()` 读取
>    - 接收输入 `proxy_list`
>    - `urlparse` 处理 `proxy`
> 4. 创建中间件，初始化 `from_crawler`
>    - @classmethod
>    - 类可以直接使用 `cls`
>    - 返回给类实例化初始接收
> 5. 设置代理 `_set_proxy`
>    - 随机选择 `random.choice()`
>    
>    - 串通整个逻辑
>    
>      ```json
>      {
>        "origin": "112.*.*.*"
>      }
>      ```



**3a\proxyspider\proxyspider\settings.py**

> 1. 所有的配置项都是大写字符；命名要有意义，无歧义
>
> 2. 开启下载中间件 `DownloaderMiddlewares`
>
>    - 将不使用的下载中间件设置为 `None`
>    - 增加 `RandomHttpProxyMiddleware`
>
>    ```python
>    DOWNLOADER_MIDDLEWARES = {
>        'proxyspider.middlewares.ProxyspiderDownloaderMiddleware': 543,
>        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
>        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
>        'proxyspider.middlewares.RandomHttpProxyMiddleware': 40,
>    
>    }
>    ```
>
> 3. 增加随机代理 `IP` 列表
>
>    ```python
>    HTTP_PROXY_LIST = [
>         'http://52.179.231.206:80',
>         'http://95.0.194.241:9090',
>    ]
>    ```



**3a\randproxy\proxyspider\spiders\httpbin.py**

> 1. name = 'httpbin'
> 2. 使用 httpbin 获取 IP `start_urls = ['http://httpbin.org/ip']`
> 3. 使用 response 直接返回信息 `print(response.text)`
> 4. 此文件代码和上节代码一样



### 1.8.3. 本节总结

> 1. 仔细阅读并学习官方代码 `HttpProxyMiddleware`
>    - site-packages\scrapy\downloadermiddlewares\httpproxy.py
>    - 逐步 print 调试；重写
> 2. 随机代理 IP：GitHub
> 3. 自定义下载中间件：步骤和思路



## 1.9. 分布式爬虫

### 1.9.1. 获取源代码

```powershell
git checkout 3b
```



### 1.9.2. 安装 **scrapy-redis**（第三方库）

```powershell
pip install scrapy-redis
```



### 1.9.3. 源代码学习

针对 scrapycluster，不变的默认 scrapy 代码

- 3b\scrapycluster\scrapy.cfg
- `3b\scrapycluster\scrapycluster\__init__.py`
- 3b\scrapycluster\scrapycluster\middlewares.py
- `3b\scrapycluster\scrapycluster\spiders\__init__.py`



**redis.conf**

```ini
bind 127.0.0.1
port 6379


daemonize yes  # 生产环境
```



**3b\scrapycluster\scrapycluster\items.py**

> 增加 `ip`
>
> ```python
> ip = scrapy.Field()
> ```



**3b\scrapycluster\scrapycluster\pipelines.py**

- 开启 `return item`



**3b\scrapycluster\scrapycluster\settings.py**

> 1. 增加 redis 信息
>
>    ```python
>    REDIS_HOST='127.0.0.1'
>    REDIS_PORT=6379
>    ```
>
> 2. Scheduler 的 QUEUE
>
>    ```python
>    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
>    ```
>
> 3. 去重
>
>    ```python
>    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
>    ```
>
> 4. Requests的默认优先级队列
>
>    ```python
>    SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
>    ```
>
> 5. 将Requests队列持久化到Redis，可支持暂停或重启爬虫
>
>    ```python
>    SCHEDULER_PERSIST = True
>    ```
>
> 6. 开启 ITEM_PIPELINES，将爬取到的 items 保存到 Redis
>
>    ```python
>    ITEM_PIPELINES = {
>        'scrapy_redis.pipelines.RedisPipeline': 300
>    }
>    ```
>



**3b\scrapycluster\scrapycluster\spiders\cluster.py**

> 1. name = 'cluster'
>
> 2. 使用 httpbin 获取 IP `start_urls = ['http://httpbin.org/ip']`
>
> 3. 返回 IP 信息 `item['ip']= json.loads(response.text)['origin']`
>
>    ```python
>    yield item
>    ```



### 1.9.4. 本节总结

> 1. Scrapy 原生不支持分布式，多机之间需要 Redis 实现队列和管道的共享
> 2. scrapy-redis 很好的实现了 Scrapy 和 Redis 的集成
> 3. 使用 scrapy-redis 之后 Scrapy 的主要变化
>    - 使用了 RedisSpider 类替代了 Spider 类
>    - Scheduler 的 queue 由 Redis 实现
>    - Item Pipeline 由 Redis 实现
> 4. 拓展 Scrapy 功能：分布式爬虫
> 5. 分布式爬虫：队列 / 管道共享
> 6. Redis
>    - 服务端 `redis-server redis.conf`
>    - 客户端 `redis-cli`
>    - Redis 数据最后再回传到 MySQL 数据库中进行储存
> 7. Scrapy 和 Redis 巧妙结合，强强联手
> 8. Scrapy 博大精深，需深入研究学习和实践
> 9. Redis 博大精深，需深入研究学习和实践





# 2. 本周作业

## 2.1. 作业一

### 2.1.1. 作业说明

- 为 Scrapy 增加代理 IP 功能
- 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制

备注：代理 IP 可以使用 GitHub 提供的免费 IP 库



### 2.1.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week02/job1



实现过程：

> 1. 为 Scrapy 增加代理 IP 功能
>
>    - 开启 DOWNLOADER_MIDDERWARE
>    - 增加随机代理 IP 列表：HTTP_PROXY_LIST
>      - https://github.com/jhao104/proxy_pool#%E5%85%8D%E8%B4%B9%E4%BB%A3%E7%90%86%E6%BA%90
>    - 增加下载中间件：RandomHttpProxyMiddleware(HttpProxyMiddleware)
>
> 2. 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制
>    - item 增加 id 属性 (对应数据库表字段)
>    - 下载部分增加异常捕获和处理机制
>    - 持久化修改为 pymysql 将数据插入 MySQL
> 3. 优化主爬虫代码
>    - 去除 start_urls (已经使用了 start_requests)
>    - parse 方法去除 sleep 方法 (页面内容已下载)
>    - 去除调试相关代码
>    - 去除 items
>    - 优化计数方法，去除 count 计数，直接使用 for 循环方法替代
>    - movie_name 优化判断规则



代码说明：

> 1. setting.py
>
>    - DOWNLOADER_MIDDLEWARES
>    - HTTP_PROXY_LIST
>
> 2. middlewares.py
>
>    - RandomHttpProxyMiddleware(HttpProxyMiddleware)
>
> 3. items.py  `id = scrapy.Field()`
>
> 4. pipelines.py  `pymysql`
>
> 5. maoyan.py
>
>    ```python
>    for movie in movies[:10]:
>        pass
>    
>    
>    if not movie_name:
>        pass
>    
>    
>    uuid5 = str(uuid.uuid5(uuid.NAMESPACE_DNS, movie_name))
>    item['id'] = ''.join(uuid5.split('-'))
>    ```



问题及解决方案：

> - [x] 02 返回地址：https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=e03539d7479647d7b25021eabd28a39e&platform=1000&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fmaoyan.com%252Ffilms%253FshowType%253D3
>   - 手动打开地址，手动滑块验证通过
> - [x] 页面下载异常：'MaoyanmovieItem does not support field: id'
>   - items.py 增加 id 字段
> - [x] pymysql.err.DataError: (1265, "Data truncated for column 'id' at row 1")
>   - 数据库字段类型和代码匹配



## 2.2. 作业二

### 2.2.1. 作业说明

使用 requests 或 Selenium 模拟登录石墨文档 [ https://shimo.im ](https://shimo.im)



作业更新：石墨文档有验证码，更换网站 https://processon.com



### 2.2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week02/job2



实现过程：

> 1. 分别使用 Selenium 和 requests 方法进行实现
> 2. 使用 Selenium 浏览器模拟实现：
>    - 使用 webdriver 关联 Chrome 浏览器
>    - 首页 - 登录，根据链接点击
>    - 根据 id: 请输入邮箱地址或者手机号码 / 请输入密码 / 立即登录
>    - 增加异常处理
> 3. 使用 requests 代码中直接 post 请求实现：
>    - 使用 fake_useragent 模拟
>    - headers 完善
>    - 使用 Session 进行会话保持
>    - form_data 必须保证一致
>    - 使用 post 方法请求
>    - 登陆成功：账户中心
>    - 增加异常处理



代码说明：

> 1. loginprocesson_by_selenium.py
>    - webdriver.Chrome()
>    - find_element_by_link_text('登录').click()
>    - find_element_by_id('login_email').send_keys('**')
>    - find_element_by_id('signin_btn').click()
>    - try / except /finally
> 2. loginprocesson_by_requests.py
>    - UserAgent(verify_ssl=False)
>    - headers 增加 `User-Agent` `Referer`
>    - requests.Session()
>    - form_data `login_email` `login_password`
>    - requests_session.post(login_url, data=form_data, headers=headers)
>    - requests_session.get(setting_url, headers=headers)
>    - try / except /finally



问题及解决方案：

> - [x] 登录失败
>   - form_data 匹配 `F12`





# 3. 学习总结

## 3.1. 收获

1. 异常处理相关知识：代码健壮性
2. 使用 pymysql 操作 MySQL：后续 ORM 期待
3. 反爬虫相关知识：UserAgent / cookies / WebDriver / 验证码 / 爬虫中间件 / 自定义中间件 / 系统代理 IP / 随机代理 IP
4. 分布式爬虫：Redis
5. 官方代码和自己写的代码，都需要不断 print 进行调试，过程中进行思考和学习



## 3.2. 问题及不足

1. 验证码识别
   - 不同操作系统准备工作
   - 更高级的验证码的识别方式
2. Selenium 相关知识
3. Redis 相关知识



## 3.3. 改进

### 3.3.1. 深入学习

1. 更多的总结和学习 BeautifulSoup 和 XPath 的相关知识
2. Selenium 相关知识加固
3. Redis 相关知识加固
4. Scrapy 深入学习；框架图；回溯其官方代码



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己
4. 反复看反复练



## 3.4. 感悟

1. 爬虫的世界博大精深，可能一个小小的问题就是一个拦路虎，反爬虫和反反爬虫的博弈世界，路漫漫兮
2. Scrapy 框架博大精深，在深入其框架原理实现的同时，其官方源码也值得学习
3. 数据库相关知识博大精深，需加强，包括 MySQL 和 Redis 相关知识
4. 学的越多越感觉到自己的不足，加油

