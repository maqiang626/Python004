# Week05-06 学习笔记 (2020.10.19 - 2020.11.8)



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
      <td>1. 开发环境配置 <br>
          2. 创建项目和目录结构 <br>
          3. 解析 settings.py 主要配置文件 <br>
          4. urls 调度器 <br>
          5. 模块和包 <br>
          6. 让 URL 支持变量 <br>
          7. URL 正则和自定义过滤器 <br>
          8. view 视图快捷方式 <br>
          9. 使用 ORM 创建数据表 <br>
          10. ORM API <br>
          11. Django 模板开发 <br>
          12. 展示数据库中的内容 <br>
          13. 豆瓣页面展示功能的需求分析 <br>
          14. urlconf 与 models 配置 <br>
          15. views 视图的编写 <br>
          16. 结合 bootstrap 模板进行开发 <br>
          17. 如何阅读 Django 的源代码 <br>
          18. manage.py 源码分析</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-11-08 21:00</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>












# 1. 课程内容知识点学习

## 1.1. 开发环境配置

### 1.1.1. 获取源代码

```powershell
git checkout 5a
```



### 1.1.2. Django 框架简介

- 开放源代码
- 全部使用 `Python` 编写：成熟的代码编写方法
- 最初⽤于管理劳伦斯出版集团旗下的⼀些以新闻内容为主的⽹站 `CMS`
- 许可证 `BSD`
- 首次发布时间：`2005` 年 `7` 月
- `MTV` 框架
- `DRY`
- 组件丰富
  - `ORM`
  - `URL` 支持正则表达式
  - `admin`
  - `auth`
  - ...
- 安装方便



### 1.1.3. 安装 **django**

```powershell
# 最新版本 3.0+ / 2.2.* (LTS)

pip install django==2.2.13

Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting django==2.2.13
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/fb/e1/c5520a00ae75060b0c03eea0115b272d6dc5dbd2fd3b75d0c0fbc9d262bc/Django-2.2.13-py3-none-any.whl (7.5 MB)
     |████████████████████████████████| 7.5 MB 38 kB/s
Requirement already satisfied: pytz in d:\maqiang\python\mdoc\advancedtrainingcamp\maqiang\venv\vatc\lib\site-packages (from django==2.2.13) (2020.1)
Collecting sqlparse
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/14/05/6e8eb62ca685b10e34051a80d7ea94b7137369d8c0be5c3b9d9b6e3f5dae/sqlparse-0.4.1-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 66 kB/s
Installing collected packages: sqlparse, django
Successfully installed django-2.2.13 sqlparse-0.4.1


>>>
>>> import django
>>> django.__version__
'2.2.13'
>>>

```



### 1.1.4. Django

```ini
# Django 2020-10-20 09:30

Name: Django
Version: 2.2.13
Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Home-page: https://www.djangoproject.com/
Author: Django Software Foundation
Author-email: foundation@djangoproject.com
License: BSD
Location: d:\maqiang\python\mdoc\advancedtrainingcamp\maqiang\venv\vatc\lib\site-packages
Requires: sqlparse, pytz
Required-by:

```



### 1.1.5. MTV 框架模式

- 模型层 `Models`

  - `Django` 提供了一个抽象的模型 ("`models`") 层，为了构建和操纵你的 `Web` 应用的数据

  - 创建模型
  - 执行 `CRUD`

- 视图层 `Views`

  - `Django` 具有 “视图” 的概念，负责处理用户的请求并返回响应

  - 接收请求
  - 调用 `Models` / 数据
  - 调用 `Templates`
  - 将数据填充到模板上再响应

- 模板层 `Templates`

  - 模板层提供了一个对设计者友好的语法用于渲染向用户呈现的信息

  - `***.html`



### 1.1.6. 本节总结

> 1. 数据采集  =>  数据清洗  =>  数据预处理  =>  数据展示
> 2. 数据展示
>    - 图片展示 `matplotlib`
>    - 多端展示 `web` 交互性 / 手机 + 平板 + 电脑
> 3. `web` 框架：`MVC` 设计模式 / `MTV` 框架
>    - 分开：表现 / 逻辑结构 / 数据存储
>      - 解耦
>    - 单个文件 `web.py`
>    - 电影 `Django`
>    - `Flask`
>    - `Tornado`
>    - `AIOHTTP`
>    - 流行 `FastAPI`
> 4. 使用 `Django` 更关注业务逻辑本身
> 5. 特定软件版本的安装方法



## 1.2. 创建项目和目录结构

### 1.2.1. 获取源代码

```powershell
git checkout 5a
```



### 1.2.2. 创建 Django 项目

```powershell
django-admin startproject MyDjango

MyDjango
│  manage.py
│
└─MyDjango
        settings.py
        urls.py
        wsgi.py
        __init__.py

```

> `MyDjango\manage.py` 
>
> - 命令行工具
> - 整个项目的管理
> - `python manage.py help`
>
> `MyDjango\MyDjango\settings.py`
>
> - 项目的配置文件
> - 整个项目的常用设置



### 1.2.3. django-admin help

```powershell
django-admin help


Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).

```



### 1.2.4. python manage.py help

```powershell
python manage.py help

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

```



### 1.2.5. 创建 Django 应用程序 (index)

```powershell
# 创建应用程序 index
python manage.py startapp index


# index 初始目录结构
index
│  admin.py   # 管理后台
│  apps.py    # 当前 app 配置文件
│  models.py  # 模型
│  tests.py   # 自动化测试
│  views.py   # 视图
│  __init__.py
│
└─migrations  # 数据库迁移文件夹
        __init__.py

```

> `templates` 需要自己手动创建



### 1.2.6. 启动 Django 应用程序 (默认)

```powershell
# 启动 Django 应用程序
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 23, 2020 - 15:15:30
Django version 2.2.13, using settings 'MyDjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


# 访问 http://127.0.0.1:8000/
The install worked successfully! Congratulations!

You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.


# RUN LOG
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 23, 2020 - 15:15:30
Django version 2.2.13, using settings 'MyDjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[23/Oct/2020 15:17:09] "GET / HTTP/1.1" 200 16348
[23/Oct/2020 15:17:09] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
Not Found: /favicon.ico
[23/Oct/2020 15:17:09] "GET /favicon.ico HTTP/1.1" 404 1974
[23/Oct/2020 15:17:10] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[23/Oct/2020 15:17:10] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[23/Oct/2020 15:17:10] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184


# 停止 Django 应用程序
CTRL + C

```



### 1.2.7. 启动 Django 应用程序 (任意网址访问)

```powershell
# 启动 Django 应用程序 (任意网址访问)
python manage.py runserver 0.0.0.0:8000

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 23, 2020 - 15:19:27
Django version 2.2.13, using settings 'MyDjango.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.

```



### 1.2.8. 本节总结

> 1. `Django`  =>  `web` 服务器
> 2. 持续运行：等待连接
> 3. 流程：三步走
>    - 创建项目
>    - 创建应用程序
>    - 启动
> 4. 安全：不用时及时关闭连接 (开发模式)



## 1.3. 解析 settings.py 主要配置文件

### 1.3.1. 获取源代码

```powershell
git checkout 5a
```



### 1.3.2. settings.py

- 项目路径
- 密钥
- 调试模式
- 域名访问权限
- `INSTALLED_APPS`：**需要修改；添加自己的 APP**
- 中间件
- 根目录访问配置 `ROOT_URLCONF`
- 模板文件
- `WSGI_APPLICATION`
- 数据库配置：**需要修改；根据实际需求进行配置**
- 密码验证
- `Internationalization`
- 静态资源



### 1.3.3. 源代码学习

**5a\MyDjango\MyDjango\settings.py**  

- [x] **Django v2.2.13** 

- [x] **Initialize: L121**

```python
"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

```

> 1. 通过注释可以查看当前使用的 `Django` 使用版本
>
>    - **L4** `Generated by 'django-admin startproject' using Django 2.2.13.`
>
> 2. 唯一导入的库 `import os`
>
>    - 方便迁移
>
> 3. 获取当前项目路径：经典方法
>
>    - [x] **Build paths inside the project like this: os.path.join(BASE_DIR, ...)**
>    - `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
>    - `pandas` 读取文件方法
>
> 4. 密钥部分：防止跨站入侵
>
>    - [x] **SECURITY WARNING: keep the secret key used in production secret!**
>
>    -  `SECRET_KEY = 'p*d7^ue2xmk+1d(5!jk_1^lk2r1jf%!+@)k3!)hjo3(c%mygsu'`
>
> 5. 调试模式：生产环境需要修改
>
>    - [x] **SECURITY WARNING: don't run with debug turned on in production!**
>    - `DEBUG = True`
>    - 单用户：阻塞
>    - 生产模式：`WSGI`
>
> 6. `APP` 列表 `Application definition`
>
>    - 不可更改系统自带 `APP` 顺序
>
>    ```python
>    INSTALLED_APPS = [
>        ####  内置的后台管理系统
>        'django.contrib.admin',
>        ####  内置的用户认证系统
>        'django.contrib.auth',
>        #### 所有 model 元数据
>        'django.contrib.contenttypes',
>        #### 会话，表示当前访问网站的用户身份
>        'django.contrib.sessions',
>        #### 消息提示
>        'django.contrib.messages',
>        #### 静态资源路径
>        'django.contrib.staticfiles',
>        #### 注册自己的 APP
>        'index',
>    ]
>    
>    ```
>
> 7. 中间件：`request` 和 `response` 对象之间的钩子 / 有顺序
>
>    ```python
>    MIDDLEWARE = [
>        'django.middleware.security.SecurityMiddleware',
>        'django.contrib.sessions.middleware.SessionMiddleware',
>        'django.middleware.common.CommonMiddleware',
>        'django.middleware.csrf.CsrfViewMiddleware',
>        'django.contrib.auth.middleware.AuthenticationMiddleware',
>        'django.contrib.messages.middleware.MessageMiddleware',
>        'django.middleware.clickjacking.XFrameOptionsMiddleware',
>    ]
>    
>    ```
>
> 8. 根目录访问配置 `ROOT_URLCONF = 'MyDjango.urls'`
>
> 9. 模板设置 `TEMPLATES`
>
>    ```python
>    TEMPLATES = [
>        {
>            #### 定义模板引擎
>            'BACKEND': 'django.template.backends.django.DjangoTemplates',
>            #### 设置模板路径：在每个应用程序里面进行具体设置
>            'DIRS': [],
>            #### 是否在 App 里查找模板文件
>            'APP_DIRS': True,
>            #### 用于 RequestContext 上下文的调用函数
>            'OPTIONS': {
>                'context_processors': [
>                    'django.template.context_processors.debug',
>                    'django.template.context_processors.request',
>                    'django.contrib.auth.context_processors.auth',
>                    'django.contrib.messages.context_processors.messages',
>                ],
>            },
>        },
>    ]
>    
>    ```
>
> 10. 数据库设置 `Database`
>
>    - 默认使用 `sqllite3`
>
>      ```python
>      DATABASES = {
>          'default': {
>              'ENGINE': 'django.db.backends.sqlite3',
>              'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>          }
>      }
>      ```
>
>    - 更改为 `MySQL`
>
>      - `Django2.2` 使用 `mysqlclient` 或 `pymysql` 模块连接 `MySQL`
>      - `export PATH=$PATH:/usr/local/mysql/bin`
>      - `OSError: mysql_config not found`
>      - `pip install mysqlclient`
>      - `pip install pymysql`
>
>      ```python
>      DATABASES = {
>          'default': {
>              'ENGINE': 'django.db.backends.mysql',
>              'NAME': 'test',
>              'USER': 'root',
>              'PASSWORD': 'rootroot',
>              'HOST': '127.0.0.1',
>              'PORT': '3306',
>          }
>          # 生产环境有可能连接第二个数据库
>          # 'db2': {
>          #     'ENGINE': 'django.db.backends.mysql',
>          #     'NAME': 'mydatabase',
>          #     'USER': 'mydatabaseuser',
>          #     'PASSWORD': 'mypassword',
>          #     'HOST': '127.0.0.1',
>          #     'PORT': '3307',
>          # }
>      }
>      ```
>
> 11. 语言 / 时区 / 国际化相关设置 `Internationalization`
>
>     ```python
>     # Internationalization
>     # https://docs.djangoproject.com/en/2.2/topics/i18n/
>     
>     LANGUAGE_CODE = 'en-us'
>     
>     TIME_ZONE = 'UTC'
>     
>     USE_I18N = True
>     
>     USE_L10N = True
>     
>     USE_TZ = True
>     
>     ```
>
> 12. 静态资源文件存放路径 `STATIC_URL = '/static/'` 
>
>     - `CSS`
>     - `JavaScript`
>     - `Images`



### 1.3.4. 本节总结

> 1. 入口：`manage.py`
> 2. 具体配置信息：`settings.py`
> 3. 区分**需要修改部分**和不需要修改部分
> 4. 所有的变量名都使用大写的形式  =>  类比 `Scrapy`



## 1.4. urls 调度器

### 1.4.1. 获取源代码

```powershell
git checkout 5a
```



### 1.4.2. Django 处理请求

1. 如果传入 `HttpRequest` 对象拥有 `urlconf` 属性（通过中间件设置），它的值将被用来代替 `ROOT_URLCONF` 设置
2. `Django` 加载 `URLConf` 模块并寻找可用的 `urlpatterns`，`Django` 依次匹配每个 `URL` 模式，在与请求的 `URL` 匹配的第一个模式停下来
3. 一旦有 `URL` 匹配成功，`Django` 导入并调用相关的视图，视图会获得如下参数：
   - 一个 `HttpRequest` 实例
   - 一个或多个位置参数提供
4. 如果没有 `URL` 被匹配，或者匹配过程中出现了异常
   - `Django` 会调用一个适当的错误处理视图
   - 可以自己编写错误返回视图



### 1.4.3. 源代码学习

**5a\MyDjango\MyDjango\urls.py**

```python
"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

```

> 1. 从 `URL` 路由到视图 (`views`) 的映射功能
>
> 2. 导入 **include** `from django.urls import path, include`
>
> 3. 从根目录访问，加载模块 `path('',include('index.urls'))`
>
> 4. `url` 访问规则
>
>    - 访问 https://127.0.0.1:8000
>
>    - **5a\MyDjango\MyDjango\settings.py**
>
>      - `ROOT_URLCONF = 'MyDjango.urls'`
>
>    - **5a\MyDjango\MyDjango\urls.py**
>
>      - `urlpatterns` 名称固定
>      - `path('',include('index.urls'))`
>      - `settings.py` 查找 `APP`
>
>    - **5a\MyDjango\index\urls.py**
>
>      - `from . import views`
>      - `path('', views.index)`
>
>    - **5a\MyDjango\index\views.py**
>
>      ```python
>      def index(request):
>          return HttpResponse("Hello Django!")
>          
>      ```
>
> 5. 对请求处理并返回



### 1.4.4. 本节总结

> 1. `urls` 接收用户的 `URL` 请求信息
> 2. `Django` 请求中间件：附带一些 `Django` 需要的信息
> 3. `URLconf` 工作逻辑
> 4. `path` 关联路径和 `view`
> 5. `include` 加载 `app`



## 1.5. 模块和包

### 1.5.1. 获取源代码

```powershell
git checkout 5a
```



### 1.5.2. 概念解析

- 模块：以 `.py` 结尾的 `Python` 程序 (一个文件)
  - 运行：`python ***.py`
    - 类
    - 函数
  - 执行：`if __name__ == '__main__':`
    - 定义和执行分开
    - 写法优雅
- 包：存放多个模块的目录
  - `__init__.py` 
    - 包运行的初始化文件
    - 可以是空文件
- 常见包的导入方式
  - `import ...`
  - `import ... as ...`
  - `from ... import ...`
  - `from ... import ... as ...`



### 1.5.3. 源代码学习

**5a\MyPackage**

> - [x] `5a\MyPackage\__init__.py`
>   - 导入包时初始化加载此文件并运行
> - [x] `5a\MyPackage\Module1.py`
>   - 以模块方式运行
>   - 自己本身运行
> - [x] `5a\MyPackage\Module2.py`
>    - 相对路径引入模块 `from . import Module1`
>     - 相对路径引入包 `from .Pkg2 import M2`
> 



### 1.5.4. 本节总结

> 1. 大量的自己编写的模块和包
>    - 自定义功能
> 2. 路径关系
> 3. 导入时防止重复导入
> 4. 引入模块或包时查找目录 `site-packages`



## 1.6. 让 URL 支持变量

### 1.6.1. 获取源代码

```powershell
git checkout 5b
```



### 1.6.2. 源代码学习

**5b\MyDjango\index\urls.py**

> 1. `path('<int:year>', views.year),` 
>    - 变量 `year`
>    - 只接收整数，其他类型返回 `404`
> 2. `path('<int:year>/<str:name>', views.name),`



**5b\MyDjango\index\views.py**

> 1. 固定写法 `request`  =>  第一个参数
>
> 2. 请求 `year`
>
>    - http://127.0.0.1:8000/202020
>
>    ```python
>    def year(request, year):
>        return HttpResponse(year)
>    
>    ```
>
>    - 请求其他页面返回 `404`
>      - http://127.0.0.1:8000/abcdef
>
> 3. 请求 `name`
>
>    - http://127.0.0.1:8000/202020/maqiang
>     - 传递两个参数 `year` `name`
>   
>    ```python
>    def name(request, **kwargs):
>        return HttpResponse(kwargs['name'])
>    
>    ```



### 1.6.3. 本节总结

> 1. `URL` 变量类型
>    - `str`
>    - `int`
>    - `slug` 备注
>    - `uuid`
>    - `path`
> 2. 一对一：特有的页面
> 3. 一类请求
>    - 变量：对类型进行处理
>      - `<int:year>`
>    - 正则表达式进行匹配
>    - 自定义函数进行匹配
> 4. 不定长参数获取形式 `**kwargs`  =>  关键字参数



## 1.7. URL 正则和自定义过滤器

### 1.7.1. 获取源代码

```powershell
git checkout 5b
```



### 1.7.2. 源代码学习

**5b\MyDjango\index\urls.py**

> 1. 导入包 `from django.urls import path, re_path, register_converter`
> 2. `re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),` 
>    - 正则匹配
> 3. 自定义规则 `path('<yyyy:year>', views.year), `
>    - 绑定 `register_converter(converters.FourDigitYearConverter, 'yyyy')`



**5b\MyDjango\index\views.py**

> 1. 固定写法 `request`
>
> 2. 请求 `myyear`
>
>    - http://127.0.0.1:8000/2020.html
>
>    ```python
>    def myyear(request, year):
>        return render(request, 'yearview.html')
>    
>    ```
>
>    - `render` 写到一个指定的文件，进行渲染，然后再返回
>      - 有利于程序解耦



**5b\MyDjango\index\converters.py**

> 1. `class IntConverter:`
>    - 必须包括三个部分
>    - 正则 `regex`
>    - 把字符串给 `Python` `to_python()`
>    - 把处理结果传给 `URL` `to_url()`
>      - 两个过程相反
> 2. `class FourDigitYearConverter:`
>    - 同样包括三部分
>    - 转化成 `URL` 格式化输出 `return '%04d' % value`



### 1.7.3. 本节总结

> 1. 正则匹配固定写法：`re_path`
>    - `?P`
> 2. 匹配顺序
>    - 从上到下
>    - 一旦匹配成功后面的不再匹配
> 3. 自定义匹配
>    - 结合正则和匹配的类型约束进行
>    - 提取出正则表达式



## 1.8. view 视图快捷方式

### 1.8.1. 获取源代码

```powershell
git checkout 5b
```



### 1.8.2. 一般响应 (HttpResponse())

- [x] **HttpResponse()**
  - `200`
  - `PermanentRedirect()`  `301`
  - `Redirect()`  `302`
  - `BadRequest()`  `400`
  - `Forbidden()`  `403`
  - `NotFound()`  `404`
  - `NotAllowed()`  `405`
  - `ServerError()`  `500`



### 1.8.3. 复杂响应 (快捷函数)

- [x] **render()**
  - 将模板文件和 `view` 视图进行绑定
  - 对 `Response` 做了一层封装
  - 将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个 `HttpResponse` 对象
- [x] **redirect()**
  - 将一个 `HttpResponseRedirect` 返回到传递的参数的适当 `URL`
  - 常用：用户名密码验证后的跳转
- [x] **get_object_or_404()**
  - 将 `view` 视图和模型进行绑定
  - 在给定的模型管理器 (`model manager`) 上调用 `get()`，但它会引发 `Http404` 而不是模型的 `DoesNotExist` 异常



### 1.8.4. 源代码学习

**5b\MyDjango\index\views.py**

> 1. `return render(request, 'yearview.html')`
>
>    - 查找模板
>      - `settings.py`  =>  `APP_DIRS`
>      - 默认名称 `templates` (目录；固定写法)
>    - 跟踪官方源代码
>      - 模块 `shortcuts.py`
>      - 函数 `render_to_string(template_name, context, ...)`
>      - 将文件和具体的内容进行了一个绑定
>
> 2. `return redirect('/2020.html')`
>
>    - 跟踪官方源代码
>      - 模块 `shortcuts.py` 
>      - 函数 `redirect_class(reslove_url, ...)`
>      - 重新解析 `URL`



**5c\MyDjango\index\templates\yearview.html**

- 变量替换 `<div><a href="{% url 'urlyear' 2020 %}">2020 booklist</a></div>`



### 1.8.5. 本节总结

> 1. 处理用户请求：`URL` 和 `view` 绑定
>    - `Python` 处理中间逻辑
> 2. 关注：处理之后的返回



## 1.9. 使用 ORM 创建数据表

### 1.9.1. 获取源代码

```powershell
git checkout 5c
```



### 1.9.2. 安装 **mysqlclient**

```powershell
pip install mysqlclient

Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting mysqlclient
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/4a/28/b08ede6cc8382179201455c3b9e5ed0d66aa5921e7c1888828dba48b832b/mysqlclient-2.0.1-cp37-cp37m-win_amd64.whl (268 kB)
     |████████████████████████████████| 268 kB 39 kB/s
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.0.1

```



### 1.9.3. ORM 创建 SQL

```powershell
# 生成中间脚本
python manage.py makemigrations

Migrations for 'index':
  index\migrations\0001_initial.py
    - Create model Name
    - Create model Type


# 生成 Migration 类
MyDjango\index\migrations\0001_initial.py


# 将中间脚本生成 SQL 表
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, index, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying index.0001_initial... OK
  Applying sessions.0001_initial... OK

```



### 1.9.4. 0001_initial.py

- [x] **MyDjango\index\migrations\0001_initial.py**

```python
# Generated by Django 2.2.13 on 2020-10-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('stars', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=50)),
            ],
        ),
    ]

```



### 1.9.5. 源代码学习

**5c\MyDjango\index\models.py**

> 1. 导入 `from django.db import models`
> 2. 类的继承 `class Type(models.Model):`
> 3. 创建两张表
> 4. `id`  =>  `Django` 会自动创建，并设置为主键
>    - `id = models.AutoField(primary_key=True)`
> 5. 创建指定字段 `name = models.CharField(max_length=50)`
> 6. 创建表的名称为：`index_Type` `index_Name`



### 1.9.6. FAQ

1. 找不到 `MySQL` 客户端？
   - `init` 方法动态生效
   - `export PATH=$PATH:/usr/local/mysql/bin`
   
2. 版本不匹配：注释相应代码

3. `str decode` 跟踪错误文件：注释

4. 安装 `mysqlclient`

   ```powershell
   >python manage.py makemigrations
   
   Traceback (most recent call last):
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\backends\mysql\base.py", line 15, in <module>
       import MySQLdb as Database
   ModuleNotFoundError: No module named 'MySQLdb'
   
   The above exception was the direct cause of the following exception:
   
   Traceback (most recent call last):
     File "manage.py", line 21, in <module>
       main()
     File "manage.py", line 17, in main
       execute_from_command_line(sys.argv)
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\core\management\__init__.py", line 381, in execute_from_command_line
       utility.execute()
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\core\management\__init__.py", line 357, in execute
       django.setup()
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\__init__.py", line 24, in setup
       apps.populate(settings.INSTALLED_APPS)
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\apps\registry.py", line 114, in populate
       app_config.import_models()
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\apps\config.py", line 211, in import_models
       self.models_module = import_module(models_module_name)
     File "E:\ToolsInstallDir\Python\Python37\lib\importlib\__init__.py", line 127, in import_module
       return _bootstrap._gcd_import(name[level:], package, level)
     File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
     File "<frozen importlib._bootstrap>", line 983, in _find_and_load
     File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
     File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
     File "<frozen importlib._bootstrap_external>", line 728, in exec_module
     File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\contrib\auth\models.py", line 2, in <module>
       from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\contrib\auth\base_user.py", line 47, in <module>
       class AbstractBaseUser(models.Model):
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\models\base.py", line 117, in __new__
       new_class.add_to_class('_meta', Options(meta, app_label))
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\models\base.py", line 321, in add_to_class
       value.contribute_to_class(cls, name)
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\models\options.py", line 204, in contribute_to_class
       self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\__init__.py", line 28, in __getattr__
       return getattr(connections[DEFAULT_DB_ALIAS], item)
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\utils.py", line 201, in __getitem__
       backend = load_backend(db['ENGINE'])
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\utils.py", line 110, in load_backend
       return import_module('%s.base' % backend_name)
     File "E:\ToolsInstallDir\Python\Python37\lib\importlib\__init__.py", line 127, in import_module
       return _bootstrap._gcd_import(name[level:], package, level)
     File "D:\maqiang\Python\MDOC\AdvancedTrainingCamp\maqiang\VENV\vatc\lib\site-packages\django\db\backends\mysql\base.py", line 20, in <module>
       ) from err
   django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
   Did you install mysqlclient?
   
   ```



### 1.9.7. 本节总结

> 1. 模型层 `Models`
>    - `CRUD`
> 2. `ORM`
>    - 类的名称  =>  表的名称
>    - 类的属性  =>  表的字段
>    - `API`
>    - 反向：表 `SQL`  =>  `ORM`
> 3. 类继承 `django.db.models.Model`



## 1.10. ORM API

### 1.10.1. 获取源代码

```powershell
git checkout 5c
```



### 1.10.2. ORM API CRUD

```powershell
# 命令行工具
python manage.py shell

Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
>>> dir()
['__builtins__']
>>>
>>> from index.models import *
>>> dir()
['Name', 'Type', '__builtins__', 'models']
>>> n = Name()
>>> n
<Name: Name object (None)>
>>> type(n)
<class 'index.models.Name'>
>>>

# 添加一条记录到 ORM ：使用属性的方式进行
>>>
>>> n.name='红楼梦'
>>> n.author='曹雪芹'
>>> n.stars=9.6
>>> n.save()
>>>

# 增加一条记录：使用 ORM 框架 API 实现
>>>
>>> Name.objects.create(name='三国演义', author='罗贯中', stars=9.5)
<Name: Name object (2)>
>>>

# 查询：经常在 view 中使用
>>>
>>> Name.objects.get(id=2).name
'三国演义'
>>>
>>> Name.objects.get(id=2)
<Name: Name object (2)>
>>>
>>>
>>> Name.objects.all()[0].name
'红楼梦'
>>>
>>> n = Name.objects.all()
>>> n[0].name
'红楼梦'
>>> n[1].name
'三国演义'
>>>
>>>
>>> Name.objects.values_list('name')
<QuerySet [('红楼梦',), ('三国演义',)]>
>>>
>>> Name.objects.values_list('name')[0]
('红楼梦',)
>>>
>>> Name.objects.values_list('name')[:]
<QuerySet [('红楼梦',), ('三国演义',)]>
>>>
>>> Name.objects.values_list('name').count()
2
>>>

# 修改
>>>
>>> Name.objects.filter(name='红楼梦').update(name='石头记')
1
>>>
>>> Name.objects.get(id=1).name
'石头记'
>>>

# 删除
>>>
>>> Name.objects.filter(name='红楼梦').delete()
(0, {'index.Name': 0})
>>>
>>> Name.objects.filter(name='石头记').delete()
(1, {'index.Name': 1})
>>>
>>> Name.objects.all().delete()
(1, {'index.Name': 1})
>>>

```



### 1.10.3. 本节总结

> 1. 对表进行增删改查：使用 `ORM` 方式
> 2. `ORM` 选项和 `SQL` 区别：一一对应
>    - 官方文档
>    - 字段类型 https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/
>    - 熟悉常用类型
>      - 整数  `AutoField`
>      - 浮点数  `FloatField`
>      - 字符  `CharField`
>      - 日期  `DateField`
> 3. `ORM` 操作结合 `Python` 本身的功能  =>  更高效



## 1.11. Django 模板开发

### 1.11.1. 获取源代码

```powershell
git checkout 5d
```



### 1.11.2. 源代码学习

**5d\MyDjango\index\templates\yearview.html**

> 1. 变量替换 `<div><a href="{% url 'urlyear' 2020 %}">2020 booklist</a></div>`
> 2. 查询 `URL`
>    - `5d\MyDjango\index\urls.py`
>    - 查询 `re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear')`
> 3. 把 `2020` 传递给 `urlyear`；再传递给前面的正则匹配：`2020.html`
> 4. 后续 `URL` 调用视图进行相应处理



### 1.11.3. 本节总结

> 1. 模板层 `Templates`
>    - `HTML`
>    - `CSS`
>    - `JS`
>    - 和 `Django` 交互：常用的 `5` 种
>      - 模板变量 `{{ variables }}`
>      - 从 `URL` 获取模板变量 `{% url 'urlyear' 2020 %}`
>      - 读取静态资源内容 `{% static "css/header.css" %}`
>      - `for` 遍历标签 `{% for type in type_list %} {% endfor %}`
>      - `if` 判断标签 `{% if name.type==type.type %} {% endif %}`
> 2. `for` 遍历
>    - 可迭代对象进行展示
>    - 结束 `endfor`
> 3. `if` 判断：类型判断
> 4. 灵活控制模板展示



## 1.12. 展示数据库中的内容

### 1.12.1. 获取源代码

```powershell
git checkout 5d
```



### 1.12.2. 页面展示获取过程

**按照如下步骤进行流程的串通：**

- [x] `5d\MyDjango\MyDjango\urls.py`
  
  - 找到 `urlpatterns` 进行匹配
  
- [x] `5d\MyDjango\index\urls.py`
  
   - 继续匹配 `urlpatterns` 和 `books` 进行匹配
   - `path('books', views.books),`
   - `from . import views`
- [x] `5d\MyDjango\index\views.py`
   - `def books(request):`
   - 获取对应的数据：使用 `ORM` 获取
     - 根据导入规则查找 `from .models import Name`
     - `n = Name.objects.all()`
   - 把本地变量 `n` 传递给模板 `bookslist.html`
     - 获取所有的本地变量 `locals()`
     - `return render(request, 'bookslist.html', locals())`
- [x] `5d\MyDjango\index\templates\bookslist.html`
  
   - `for` 循环遍历：传递变量 `n`
   
   - 两个 `div` 标签
   
   - 可以使用表格更美观输出
   
   - 可以加上 `css` 样式
   
     ```html
     {% for book in n %}
         <div>bookname: {{ book.name }}   <br>
                author: {{ book.author }} <br>
                stars:  {{ book.stars }}  
         </div>
     {% endfor %}
     
     ```
   
     

### 1.12.3. 本节总结

> 1. 串通 `MTV` 框架
> 2. 首先运行 `runserver`  =>  首页  =>  `/books` 展示
> 3. 优化展示
>    - 增加验证功能
>    - 增加用户功能
>    - 增加样式表



## 1.13. 豆瓣页面展示功能的需求分析

### 1.13.1. 获取源代码

```powershell
git checkout 5e
```



### 1.13.2. 需求分析

- [x] `URLConf` 对网址进行处理
  - 到达展示页面
- [x] `MTV` 和 `URLConf` 进行结合
  - `Models` 数据库模型 `ORM`
  - `Views` 通过 `Model` 取出什么样的数据
  - `Template` 展示：需要结合前端框架并填充数据
- [x] 展示：页面部分包含具体内容
  - `Dashboard` 部分
  - 四个汇总部分：评论数量 / 平均星级 / 情感倾向 / 正向数量
    - 存入数据库
  - 舆情数据展示：列出所有数据
  - 图表展示：正向评价和负向评价



### 1.13.3. 本节总结

> 1. `Django` 框架和 `web` 前端框架结合
> 2. 前端框架：`SB Admin v2.0`
> 3. 整体功能包含哪些元素  =>  都如何获得  =>  如何实现
> 4. 相关数据通过爬虫：存入数据库



## 1.14. urlconf 与 models 配置

### 1.14.1. 获取源代码

```powershell
git checkout 5e
```



### 1.14.2. 源代码学习

- [x] **URLS 解析：如下三部分 (按照顺序)** 

**5e\MyDjango\MyDjango\settings.py**

> 1. `INSTALLED_APPS` 注册 `APP`
> 2. 加载 **APP** `python manage.py runserver`



**5e\MyDjango\MyDjango\urls.py**

> 1. **douban APP** `path('douban/',include('Douban.urls')),`
> 2. `douban/` 后面必须有反斜线；自动进行路径拼接
> 3. 通过 `include` 进行查找
> 4. 通过 `urls` 组合多个 `APP`



**5e\MyDjango\Douban\urls.py**

> 1. 此文件完全新建
> 2. 导入 `from django.urls import path`
> 3. 组合路径 `path('index', views.books_short),`
>    - 拼接成完整路径 http://ip:port/douban/index



- [x] **Models 解析**

**5e\MyDjango\Douban\urls.py**

> 1. 导入 `from . import views`
> 2. 指定当前 **APP views** `path('index', views.books_short),`



**5e\MyDjango\Douban\views.py**

> 1. `views` 从 `Models` 获取数据
> 2. `views` 然后通过 `render` 进行模板渲染
> 3. 从当前 `Models` 获取 `T1`
>    - `from .models import T1`



**5e\MyDjango\Douban\models.py**

> 1. 反向创建 `T1`
>
>    - `python manage.py inspectdb`
>      - 输出重定向生成 `models.py`
>    - 将 `MySQL` 表转换成 `Models`
>
> 2. 元数据 `Meta` 不属于任何一个字段的数据
>
>    ```python
>    class Meta:
>        managed = False
>        db_table = 't1'
>    ```
>
>    - `managed = False` 不能通过 `ORM` 转换成数据库中的表
>      - 防止出现数据冲突
>    - `db_table = 't1'` 若不指定；默认为 `Douban_T1`
>    - 自己创建 `Models` 没有指定 `Meta` 数据，默认为 `True`
>
> 3. 通过 `settings.py` 里面的数据库连接进行设置
>
>    - `5e\MyDjango\MyDjango\settings.py`



### 1.14.3. 本节总结

> 1. 功能拆分
>    - 主页和单独功能
>      - 新功能和原始功能是否有耦合
>      - 没有关联就新建一个 `APP`
>    - 规划好总体结构：直接创建 `APP`；后续通过 `URLConf` 串联
> 2. 功能简单：一个 `APP` 即可
> 3. 配置 `urls` ：在项目中进行组合访问
> 4. 原生项目：通过 `ORM` 创建 `Models`  **(正向)**
> 5. 使用 `Scrapy`：数据存入 `MySQL`
>    - 从 `MySQL` 创建 `Models`  **(反向)**
> 6. 注意正向和反向 `ORM` 之间的关系



## 1.15. views 视图的编写

### 1.15.1. 获取源代码

```powershell
git checkout 5e
```



### 1.15.2. 源代码学习

**5e\MyDjango\Douban\views.py**

> 1. 导入 `from .models import T1`
> 2. 根据具体页面内容进行相应功能的编写
> 3. 参考官方文档查找具体帮助信息
>    - https://docs.djangoproject.com/zh-hans/2.2/
>    - **QuerySet**  执行查询  https://docs.djangoproject.com/zh-hans/2.2/topics/db/queries/
>      - `Managers` 只能通过模型类访问，而不是通过模型实例，目的是强制分离 “表级” 操作和 “行级” 操作
>      - `Manager`  管理器默认名称  =>  `objects`
> 4. **QuerySet** `shorts = T1.objects.all()`
>    - `Python` 方法处理
>      - 数量 `count()`
>      - 过滤 `filter()` https://docs.djangoproject.com/zh-hans/2.2/topics/db/queries/#retrieving-specific-objects-with-filters
>      - 聚合 `aggregate()` https://docs.djangoproject.com/zh-hans/2.2/topics/db/aggregation/
>    - 管理器方法处理
>      - 取某一列信息 `values('sentiment')`
> 5. 表达式 `sentiment__gte`  =>  **双下划线连接字段和比较运算符**
>    - 大于 `gt`
>    - 大于等于 `gte`
>    - 小于 `lt`
>    - 小于等于 `lte`
> 6. 聚合：平均值 `Avg`
>    - 聚合的官方定义
>    - `star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "`
>    - https://docs.djangoproject.com/zh-hans/2.2/topics/db/aggregation/#generating-aggregates-over-a-queryset



### 1.15.3. 本节总结

> 1. `view`  =>  结合 `URLconf` 和 `Models`
> 2. 默认模型管理器 `objects`
> 3. `SQL` 语句  =>  转换成 `ORM` 语法
>    - `show tables;`
>    - `desc t1;`
>    - `select * from t1 limit 2\G`
> 4. `view` 相关代码优雅性可以进行优化



## 1.16. 结合 bootstrap 模板进行开发

### 1.16.1. 获取源代码

```powershell
git checkout 5e
```



### 1.16.2. 源代码学习

**5e\MyDjango\Douban\templates\index.html**

> 1. 对应：右边主页面部分
> 2. `row` 对应页面 `4` 个卡片
>    - `div class="col-lg-3 col-md-6"`
> 3. 下面 `8` 格和 `4` 格
>    - `div class="col-lg-8"`
>    - `div class="col-lg-4"`



**5e\MyDjango\Douban\templates\base_layout.html**

> 1. 对应页面：侧边栏
> 2. 增加：统计结果展示
>    - **L263**  `<a href="index"><i class="fa fa-result fa-fw"></i> 统计结果展示</a>`
>    - 转到 `urls.py`
>      - `5e\MyDjango\Douban\urls.py`
> 3. `5e\MyDjango\Douban\urls.py`
>    - `path('index', views.books_short),`
> 4. `5e\MyDjango\Douban\views.py`
>    - `return render(request, 'result.html', locals())`



**5e\MyDjango\Douban\templates\result.html**

> 1. 模板的继承  **L1**
>    - `{% extends "base_layout.html" %}`  
>    - `{% block title %}Welcome{% endblock %}` 
> 2. 引入文件  **L2**
>    -  `{% load static %}`
> 3. 文件头部信息
>    - **L3** `{% block head %}`
>    - **L4** 保留继承的原有内容 `{{ block.super }}`
>    - 再增加新的标签  **L5 L6**
>      - `<link rel="stylesheet" href="{% static 'css/timeline.css' %}">`
>      -   `<link rel="stylesheet" href="{% static 'css/morris.css' %}">`
>      -   若重复，子标签会覆盖父标签
>    - **L7** `{% endblock %}`
> 4. `8` 格：表格展示详细信息
>    - **L108**   `<div class="col-lg-8">`
>    - **L129**  迭代获取具体内容 `{% for short in shorts %}`
> 5. `4` 格：饼图
>    - **L154**  `<div class="col-lg-4">`
>    - 数据通过 `js` 获取
>      - `5e\MyDjango\Douban\static\js\morris-data.js`
>    - **L161**  数据通过变量传入
>      - `<div id="morris-donut-chart" lg05={{ plus }} lt05={{ minus }}></div>`



**5e\MyDjango\Douban\static\js\morris-data.js**

> 1. 根据 `id` 对应 **L2 L3**
>    - `let lg05 = $("#morris-donut-chart").attr('lg05')`
>    - `let lt05 = $("#morris-donut-chart").attr('lt05')`
> 2. `lg` 和 `lt` 在 `js` 中进行相应的展示
> 3. 可以修改为 `ajax` 方式



### 1.16.3. 本节总结

> 1. `view` 把 `models` 数据传递给 `templates` 模板
> 2. 前端框架 `bootstrap`
>    - `SB ADMIN 2`  官方网站
>    - 查看官方文档进行学习
>    - 栅格系统：页面适配能力
>      - `.container` 浏览器宽度分成 `12` 格
> 3. `static` 目录：`Django` 会自动查找此目录
>    - `css`
>      - `5e\MyDjango\Douban\static\css\bootstrap.min.css`
>    - `fonts`
>    - `images`
>    - `js`
>      - `5e\MyDjango\Douban\static\js\bootstrap.min.js`
>      - `5e\MyDjango\Douban\static\js\jquery.js`
> 4. 完成页面展示：`URLconf` 结合 `MTV`



## 1.17. 如何阅读 Django 的源代码

### 1.17.1. 获取源代码

```powershell
git checkout 5e
```



### 1.17.2. 源代码学习

**5e\MyDjango\manage.py**

> 1. 定义函数 `main()`
> 2. `if __name__ == '__main__':`
>    - 优雅写法
>    - `python manage.py`
>      - `__name__ == '__main__'`
>    - `import manage`
>      - `__name__ == 'manage'`
> 3. 根据某一个单一功能进行跟踪
> 4. 搜索源代码查找某一个变量的功能
> 5. 横向：搜索某一参数功能 (非常多的参数)
> 6. 运行：`python manage.py runserver 8080`
> 7. 根据作用进行逐条分析：五步走
>    - 解析所有的参数 `python manage.py runserver 8080`
>    - 加载模块 `runserver`
>    - 检查 `INSTALLED_APPS` `IP` `PORT` `ORM`
>    - 实例化 `WSGIserver` 接收用户的 `HTTP` 请求
>    - 动态创建类，真正接收请求



### 1.17.3. 本节总结

> 1. 深入学习 `Django`
>    - 官方文档：全面熟悉基本功能
>    - 其他人代码
>    - 阅读 `Django` 本身的源代码
> 2. 好处
>    - 编写优雅程序
>    - 更深入理解 `Django` ；便于深入开发 `Django`
>    - `Python` 高级特性的应用
>      - 基础语法到高级语法的进阶
> 3. 阅读源代码：为什么  =>  怎么做
> 4. 动态语言：程序入口  =>  `manage.py`



## 1.18. manage.py 源码分析

### 1.18.1. 获取源代码

```powershell
git checkout 5e
```



### 1.18.2. manage.py

```python
# Django v2.2.13


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```



### 1.18.3. 源代码学习

**5e\MyDjango\manage.py**

> 1. 注册环境变量
>
>    - `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')`
>    - 便于其他应用程序快速查找
>
> 2. 导入进行校验 `try except`
>
>    - `from django.core.management import execute_from_command_line`
>    - 导入失败：没有安装 `Django`
>
> 3. 执行函数 `execute_from_command_line(sys.argv)`
>
>    - `python manage.py runserver 8080`
>
>    - 参数代入后代码
>
>      ```python
>      execute_from_command_line(('manage.py', 'runserver', '8080'))
>      ```
>
> 4. 跟踪官方代码 `execute_from_command_line()`
>
>    - 具体位置 `django\core\management\__init__.py`  **L382**
>
>    - 回到此文件 `__init__.py` 代码最上面：**导入了很多重要功能**
>    
>    - **L151** `ManagementUtility`  类  `django\core\management\__init__.py`
>    - **fetch_command**  **L195** `ManagementUtility`  类  `django\core\management\__init__.py`
>    - 导入模块 `runserver.py`
>    - 拼接命令：`runserver.py.Command().run_from_argv(self.argv)`
>    
> 5. 命令和参数分开处理
>



**`django\core\management\__init__.py`**  **L382**

> 1. `__init__.py` 初始化功能
>
> 2. `execute_from_command_line(argv=None)`
>
>    ```python
>    def execute_from_command_line(argv=None):  # MQ: L378
>        """Run a ManagementUtility."""
>        utility = ManagementUtility(argv)
>        utility.execute()
>        
>    ```
>
> 3. 回到此文件 `__init__.py` 代码最上面：**导入了很多重要功能**
>
>    ```python
>    from collections import OrderedDict, defaultdict  # MQ: L5 有序字典 默认工厂字典
>    
>    from django.conf import settings  # MQ: L11
>    from django.core.exceptions import ImproperlyConfigured  # MQ: 异常处理
>    from django.core.management.base import (
>        BaseCommand, CommandError, CommandParser, handle_default_options,
>    )
>    
>    ```
>
> 4. **L151** `ManagementUtility`  类
>
>    ```python
>    class ManagementUtility:
>        """
>        Encapsulate the logic of the django-admin and manage.py utilities.
>        """
>        def __init__(self, argv=None):
>            self.argv = argv or sys.argv[:]      # MQ: L155 初始化
>            
>            
>        def execute(self):   # MQ: L301
>            """
>            Given the command-line arguments, figure out which subcommand is being
>            run, create a parser appropriate to that command, and run it.
>            """
>            try:
>                subcommand = self.argv[1]    # MQ: subcommand = runserver
>            except IndexError:
>                subcommand = 'help'  # Display help if no arguments were given.   
>            try:    # MQ: L324
>                settings.INSTALLED_APPS    # MQ: L11 引入 settings (注册自己的 APP) 对 ORM 进行读取检查
>            except ImproperlyConfigured as exc:
>                self.settings_exception = exc
>            except ImportError as exc:
>                self.settings_exception = exc
>            
>            if subcommand == 'runserver' and '--noreload' not in self.argv:  # MQ: L335 检查
>                    try:
>                        autoreload.check_errors(django.setup)()
>                
>                
>             self.fetch_command(subcommand).run_from_argv(self.argv)  # MQ: L375
>            # MQ: 传参之后语句: self.fetch_command(runserver).run_from_argv(8080)
>            
>    ```
>
> 5. **L195** **fetch_command**  `ManagementUtility`  类
>
>    ```python
>    def fetch_command(self, subcommand):
>            """
>            Try to fetch the given subcommand, printing a message with the
>            appropriate command called from the command line (usually
>            "django-admin" or "manage.py") if it can't be found.
>            """
>            # Get commands outside of try block to prevent swallowing exceptions
>            commands = get_commands()  # MQ: 获取命令列表
>            try:
>                app_name = commands[subcommand]  # MQ: app_name = commands[runserver]
>            except KeyError:
>                if os.environ.get('DJANGO_SETTINGS_MODULE'):
>                    # If `subcommand` is missing due to misconfigured settings, the
>                    # following line will retrigger an ImproperlyConfigured exception
>                    # (get_commands() swallows the original one) so the user is
>                    # informed about it.
>                    settings.INSTALLED_APPS
>                else:
>                    sys.stderr.write("No Django settings specified.\n")
>                possible_matches = get_close_matches(subcommand, commands)
>                sys.stderr.write('Unknown command: %r' % subcommand)
>                if possible_matches:
>                    sys.stderr.write('. Did you mean %s?' % possible_matches[0])
>                sys.stderr.write("\nType '%s help' for usage.\n" % self.prog_name)
>                sys.exit(1)
>            if isinstance(app_name, BaseCommand):  # MQ: 现有的 runserver 是否已经被加载
>                # If the command is already loaded, use it directly.
>                klass = app_name
>            else:
>                klass = load_command_class(app_name, subcommand)  # MQ: 再加载
>            return klass
>        
>        
>    def load_command_class(app_name, name):  # MQ: L30
>        """
>        Given a command name and an application name, return the Command
>        class instance. Allow all errors raised by the import process
>        (ImportError, AttributeError) to propagate.
>        """
>        module = import_module('%s.management.commands.%s' % (app_name, name))  # MQ: 开始真正导入模块 import_module
>        return module.Command()  # MQ: 执行模块的命令
>        
>    ```
>
> 6. 调用模块



**django\contrib\staticfiles\management\commands\runserver.py**

> 1. 导入模块 `runserver`
>
>    ```python
>    class Command(RunserverCommand):  # MQ: L8 (包含 2 个函数) 父类：RunserverCommand
>        def get_handler(self, *args, **options):  # MQ: L22
>            """
>            Return the static files serving handler wrapping the default handler,
>            if static files should be served. Otherwise return the default handler.
>            """
>            handler = super().get_handler(*args, **options):  # MQ: L27
>            
>    ```
>
> 2. 此文件没有 `run_from_argv()`  =>  跟踪父类 `RunserverCommand`
>
> 3. `get_handler`  =>  `WSGI`



**django\core\management\commands\runserver.py**

> 1. 父模块 `RunserverCommand`
>
>    ```python
>    class Command(BaseCommand):  # MQ: L23 父类：BaseCommand
>        help = "Starts a lightweight Web server for development."
>    
>        # Validation is called explicitly each time the server is reloaded.
>        requires_system_checks = False
>        stealth_options = ('shutdown_message',)
>    
>        default_addr = '127.0.0.1'  # MQ: 一系列初始化默认设置操作
>        default_addr_ipv6 = '::1'
>        default_port = '8000'
>        protocol = 'http'
>        server_cls = WSGIServer
>        
>        def get_handler(self, *args, **options):
>            """Return the default WSGI handler for the runner."""
>            return get_internal_wsgi_application()  # MQ: L64
>            
>    ```
>
> 2. 此文件没有 `run_from_argv()`  =>  继续跟踪父类 `BaseCommand`



**django\core\management\base.py**

> 1. 父模块 `BaseCommand`
>
>    ```python
>    class BaseCommand:  # MQ: L148
>         def run_from_argv(self, argv):  # MQ: L306
>            """
>            Set up any environment changes requested (e.g., Python path
>            and Django settings), then run this command. If the
>            command raises a ``CommandError``, intercept it and print it sensibly
>            to stderr. If the ``--traceback`` option is present or the raised
>            ``Exception`` is not ``CommandError``, raise it.
>            """
>            self._called_from_command_line = True
>            parser = self.create_parser(argv[0], argv[1])
>    
>            options = parser.parse_args(argv[2:])
>            cmd_options = vars(options)
>            # Move positional args out of options to mimic legacy optparse
>            args = cmd_options.pop('args', ())
>            handle_default_options(options)
>            try:
>                self.execute(*args, **cmd_options)  # MQ: L323
>            
>        def execute(self, *args, **options):  # MQ: L342
>            """
>            Try to execute this command, performing system checks if needed (as
>            controlled by the ``requires_system_checks`` attribute, except if
>            force-skipped).
>            """
>            
>    ```
>
> 2. `execute()` 没有在当前类进行执行
>
>    - 由孙类而来 `runserver`
>    - 同时运行也由孙类来运行
>    
> 3. 标准输入输出
>
> 4. 连接数据库进行操作



**django\core\servers\basehttp.py**

> 1. `get_handler()` 跟踪
>
>    ```python
>    def get_internal_wsgi_application():
>        """
>        Load and return the WSGI application as configured by the user in
>        ``settings.WSGI_APPLICATION``. With the default ``startproject`` layout,
>        this will be the ``application`` object in ``projectname/wsgi.py``.
>    
>        This function, and the ``WSGI_APPLICATION`` setting itself, are only useful
>        for Django's internal server (runserver); external WSGI servers should just
>        be configured to point to the correct application object directly.
>    
>        If settings.WSGI_APPLICATION is not set (is ``None``), return
>        whatever ``django.core.wsgi.get_wsgi_application`` returns.
>        """
>        from django.conf import settings
>        app_path = getattr(settings, 'WSGI_APPLICATION')
>        if app_path is None:
>            return get_wsgi_application()  # MQ: L42
>    ```
>
> 2. 跟踪 `get_wsgi_application()`



**django\core\wsgi.py**

> 1. `get_wsgi_application()` 跟踪
>
>    ```python
>    import django
>    from django.core.handlers.wsgi import WSGIHandler
>    
>    
>    def get_wsgi_application():
>        """
>        The public interface to Django's WSGI support. Return a WSGI callable.
>    
>        Avoids making django.core.handlers.WSGIHandler a public API, in case the
>        internal WSGI implementation changes or moves in the future.
>        """
>        django.setup(set_prefix=False)
>        return WSGIHandler()
>        
>    ```
>
> 2. `WSGIHandler()` 初始化  =>  接收用户请求



**`django\conf\__init__.py`**

> 1. 执行过程中串联此文件
>
> 	```python
> 	settings = LazySettings()     # MQ: L255 此文件由前面一个文件 L11 跳转过来
>     
> 	class LazySettings(LazyObject):  # MQ: 加载 settings.py 这个配置文件的过程
>     
>    ```
> 
> 2. 后续对 `ORM` 进行检查
>




### 1.18.4. 本节总结

> 1. `runserver` 五件事情
>    - 解析 `manage.py` 的两个参数
>    - `commands/runserver.py` 多继承
>    - 检测相关配置  =>  `INSTALLED_APP`  `IP` `PORT`
>    - `get_handler()` 实例化 `WSGIHandler()`  =>  多线程模型
>    - 动态创建接收用户请求的类
> 2. 阅读源代码好处
>    - 理解 `runserver` 整个流程
>      - 方便定位流程环节中问题
>      - 可以自己修改源代码
>    - 更深入理解 `Python` 特性
> 3. 通过分析 `manage.py` 串通整个执行过程





# 2. 本周作业

## 2.1. 作业说明

**作业背景**

数据经过分析和清洗之后，需要使用适当的方式对数据进行展示，Web 就是当前最流行的展示方式之一。

**作业要求**

使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：

1. 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
2. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
3. （选做）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。

**注意**

如果你对前端相关的技术不太熟悉，我们在页面下方提供了前端模版（frontend.zip 文件），可以直接在作业中使用。



## 2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week05/job



实现过程：

> 1. 使用 `requests` 爬取电影短评相关信息
> 2. `Django` 相关知识串通



代码说明：

> 1. 代码 `job\getmovieinfo.py`
> 2. 关键代码 `job\ShowMovie\douban\views.py`



问题及解决方案：

> - [x] 日期格式 `Oct. 28, 2005, midnight`
>   - `{{ movie.comment_time | date:"Y-m-d" }}`
> - [x] 固定 `nav`
>   - 自定义 `style`





# 3. 学习总结

## 3.1. 收获

1. `Django` 搭建和配置
2. 熟悉 `URLConf` 和 `MTV` 框架
3. 整个流程串通



## 3.2. 问题及不足

1. `Django` 源代码理解还不够
2. 实际在生产环境中使用 `Django` 总感觉不够
3. 前端相关知识薄弱



## 3.3. 改进

### 3.3.1. 深入学习

1. `Django` 源代码学习
2. 前端相关知识



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

1. `Django` 知识博大精深
2. 前端知识博大精深
3. 反复把教程看了几遍，基本对 `Django` 框架熟悉，但是应用到生产环境感觉不够
4. 期待后续 `Django` 进阶教程

