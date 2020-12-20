# Week11-12 学习笔记 (2020.11.29 - 2020.12.20)



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
      <td>1. Django 源码分析之 URLconf 的偏函数 <br>
          2. Django 源码分析之 URLconf 的 include <br>
          3. Django 源码分析之 view 视图的请求过程 <br>
          4. Django 源码分析之 view 视图的响应过程 <br>
          5. Django 源码分析之 view 视图的请求响应完整流程 <br>
          6. Django 源码分析之 model 模型的自增主键创建 <br>
          7. Django 源码分析之 model 模型的查询管理器 <br>
          8. Django 源码分析之 template 模板的加载文件 <br>
          9. Django 源码分析之 template 模板的渲染 <br>
          10. Django Web 相关功能 - 管理界面 <br>
          11. Django Web 相关功能 - 表单 <br>
          12. Django Web 相关功能 - 表单 CSRF 防护 <br>
          13. Django Web 相关功能 - 用户管理认证 <br>
          14. Django Web 相关功能 - 信号 <br>
          15. Django Web 相关功能 - 中间件 <br>
          16. Django 相关功能 - 生产环境部署 <br>
          17. Django 相关功能 - celery 介绍 <br>
          18. Django 相关功能 - celery 定时任务的实现 <br>
          19. Flask 上下文与信号 <br>
          20. Tornado 简介与其他常见网络框架对比</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-12-20 21:10</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>










# 第十一、十二周：Django 开发进阶

# 1. 课程内容知识点学习

## 1.1. Django 源码分析之 URLconf 的偏函数

### 1.1.1. 获取源代码

```powershell
git checkout 7b
```



### 1.1.2. 源代码学习

**7b\MyDjango\index\urls.py**

> 1. 区分  `path`  和  `re_path`
> 2. 跟踪  `path`  官方源代码
> 



**site-packages\django\urls\conf.py**

> 1. `L76`  `path = partial(_path, Pattern=RoutePattern)`
> 2. 跟踪  `partial`  路径
>    - 不同场景下固定某些参数
>    - 标准库  `Python37\lib\functools.py`
>    - 官方网站标准库文档介绍《标准库参考》
>      - 相关所有内容
>      - 原理实例代码：具体实现方法
>      - 官方  `Demo`  =>  方便记忆和理解
>      - 装饰器
> 3.  `partial`  注意事项
>    - 第一个参数必须是可调用对象
>    - 参数传递顺序是从左到右，但不能超过原函数参数个数
>    - 关键字参数会覆盖  `partial`  中定义好的参数
> 4. `partial`  函数的实现
>    - 闭包 (装饰器)
>    - 怎么实现参数处理
>    - 除了实现功能，还考虑了哪些额外的功能
>      - 输入信息进行类型转换
>      - 异常处理
>      - ...
> 



### 1.1.3. 本节总结

> 1. `Django` 最主要的几个逻辑的代码
>    - 最常用
>    - 最基本
> 2. 主要包括四个部分
>    - `URLConf`  处理用户请求路径
>    - `View`  关联模型和模板
>    - `Template`  模板
>    - `Model`  查询管理器  `object`
> 3. 怎么样学习源代码



## 1.2. Django 源码分析之 URLconf 的 include

### 1.2.1. 获取源代码

```powershell
git checkout 7b
```



### 1.2.2. 源代码学习

**7b\MyDjango\MyDjango\urls.py**

> 1. include  加载其他文件
>2. 跟踪  include  官方代码
> 



**site-packages\django\urls\conf.py**

> 1. `L12`  `def include(arg, namespace=None):`
> 2. `L14`  `include`  如果是元组类型进行拆分
> 3. `L33`  `include`  如果是字符串类型，获得两个新的属性并返回  `urlconf_module`  对象本身
> 4. `L34`  `import_module`
>    - 考虑额外的功能
>    - 当作模块进行导入：可能存在多个值
>      - 取列表值  `getattr`  =>  `urlpatterns`
> 5. 获取导入的文件的  `url_pattern`，最终会获得  `douban.urls`  的  `urlpatterns`
> 6. 最后返回：返回列表或  `URLConf`  模块，`app_name`  `namespace`  可能为空
> 



### 1.2.3. 本节总结

> 1. `include`  引入另外一个文件
> 2. 定义一些全局设置  =>  加载子模块设置
> 3. 通读此文件  `site-packages\django\urls\conf.py`
>    - 每一部分的具体应用
>    - `_path()`
>    - `import_module()`
>    - ...
> 4. `URLconf`  两个功能
>    - 偏函数  =>  降低函数调用的难度
>    - `include`  =>  把子项目当中类型去做一个拆分
> 5. 深入分析和总结



## 1.3. Django 源码分析之 view 视图的请求过程

### 1.3.1. 获取源代码

```powershell
git checkout 7b
```



### 1.3.2. 源代码学习

**7b\MyDjango\index\views.py**

> 1. `L17`  `def myyear(request, year):`
> 2. 第一个参数  `request`
> 3. `from django.http import HttpRequest`  =>  跟踪官方代码
>    - `HttpRequest`  变成  `request`
>    - 初始化加载  `manage.py`  通过  `wsgi`  创建实现
> 4. `from django.http import HttpResponse`
>    - `HttpResponse`  由开发者创建实现
> 



**site-packages\django\http\request.py**

> 1. `L40`  `class HttpRequest:`
> 2. 发起请求
> 3. 初始化  `L47`  `def __init__(self):`
>    - 初始化元数据  `META`
>    - 做相应的拆分
> 4. `QueryDict`  `MultiValueDict`  =>  `Django`  自带的工具  `utils`
>    -  `L391`  `class QueryDict(MultiValueDict):`
>    - `site-packages\django\utils\datastructures.py`
>      -  `L44`  `class MultiValueDict(dict):`
>      - 支持多个值
> 5. 运行网站进行验证
> 6. 发起  `get`  请求  http://127.0.0.1:8080/?id=1&name=maqiang
> 7. 拆分参数：调试模式进行查看
> 8. 参数名字重复  `/?id=1&id=2`  =>  `QueryDict`  特殊字典进行处理
>    - `print(request.GET)`
>      - 输出  `<QueryDict: {'id': ['1', '2'], 'name': ['maqiang']}>`



### 1.3.3. 本节总结

> 1. `MTV`  模式
> 2. 请求和返回的流程
> 3. 常用属性和方法的熟悉  `site-packages\django\http\request.py`



## 1.4. Django 源码分析之 view 视图的响应过程

### 1.4.1. 获取源代码

```powershell
git checkout 7b
```



### 1.4.2. 源代码学习

**7b\MyDjango\index\views.py**

> 1. `L36`  `response2 = HttpResponse("Any Text", content_type="text/plain")`
> 2. 打开网站进行调试  =>  关注  `HTTP`  头部信息
>    - 返回中间件进行自动添加
> 3. 自定义头部信息  =>  关键字参数
>    - 修改头部信息
> 4. #########
> 5. 使用  `HttpResponse`  的子类  =>  官方文档
> 6. 导入  `from django.http import JsonResponse`
> 7. 导入  `from django.http import HttpResponseNotFound`
>    - `status_code = 404`
> 8. 请求中间件  =>  进行隔离和验证



**site-packages\django\http\request.py**

> 1. `L40`  `class HttpRequest:`
> 2. 发起请求



### 1.4.3. 本节总结

> 1. `View`  视图两种响应返回
>    - 返回  `HTTPResponse`  对象
>    - 产生错误，抛出异常
> 2. `HttpResponse`  定义  =>  官方文档
>    - 指定  `Django`  版本
>    - 通过关键字进行搜索
>    - 查看定义
>    - 重要属性
>    - 重要方法
>    - 查看示例
> 3. 自定义  `HttpResponse`  子类
>    - 自定义返回值
> 4. 阅读源代码
>    - 更灵活的去掌握  `Django`
>    - 知识可以推导得出



## 1.5. Django 源码分析之 view 视图的请求响应完整流程

### 1.5.1. 获取源代码

```powershell
git checkout 7b
```



### 1.5.2. Django Flowchart

![DjangoFlowChart](./120909_1217_DjangoFlowc1.png)

- **官方说明**  `number`
  1. User requests a page
  2. Request reaches Request Middlewares, which could manipulate or answer the request
  3. The URLConffinds the related View using urls.py
  4. View Middlewares are called, which could manipulate or answer the request
  5. The view function is invoked
  6. The view could optionally access data through models
  7. All model-to-DB interactions are done via a manager
  8. Views could use a special context if needed
  9. The context is passed to the Template for rendering
- **官方说明**  `letter`
  - a. Template uses Filters and Tags to render the output
  - b. Output is returned to the view
  - c. HTTPResponse is sent to the Response Middlerwares
  - d. Any of the response middlewares can enrich the response or return a completely new response
  - e. The response is sent to the user’s browser.
- **官方解释**
  - [x] In step #9 in the diagram shouldn’t the arrow be between Template-View instead of Template-Model?
    Step #8, #9 and #b are slightly mixed up. Will need to revise the diagram.
- **学习**
  - `Browser`  =>  通过浏览器请求 `http` 协议的客户端
  - **1** `modwsgi`  =>  `manage.py`  启动  `WSGIhandler`  句柄
    - `Web Server Gateway Interface`  服务器网关接口，一种规范
    - 开发环境部署
    - 生产环境部署
  - 每次新的请求：通过 `HttpRequest` 类的实例 `request`，每次请求都带着这个实例，作为第一个参数；从请求到整个的返回都带着自己的请求的对象
    - 默认  `Request` `GET` 方法
    - `POST` 方法不包含上传文件数据； `_files` 属性
    - `multipart` / `form-data` 才会有数据
  - **2** 先到请求中间件
    - 全局预处理
    - 反爬虫 / `cookies` / `Http` 头部信息
    - 返回中间件：`404` / `418` / 安全性验证 / 跨站攻击 `CSRF`
  - **3**  `URLConf` `urls.py`
  - **4** `View Middlewares`  中间件 / 页面不存在
  - **5** `View` `views.py` 自己编写的代码 / `404`
  - **6** `Model` `models.py`  模型
  - **7** `Managers` 扩展 / 模型的查询管理器 `object`
  - **8** `Context` 上下文  =>  `View` 和 `Model` 解耦
  - **a** `Template` 自己编写的模板，通过 `Filters` / `Tags` 绑定模板，替换变量，渲染输出
  - **b** `Template` 到 `Model`，再到 `View`
  - **c** `View` 到 `Response`
  - **d** 无论什么样的返回都经过返回中间件，返回给 `wsgi` 模块，交给 `modwsgi`
  - **e** `modwsgi` 返回给浏览器
- **理解**
  - `Django`  =>  自己实现的代码
  - `Your code`  =>  程序员需要实现的代码
  - `Extendable` 中间件  =>  扩展代码
  - `External`  =>  外部工具
    - 浏览器
    - 数据库



### 1.5.3. 本节总结

> 1. 处理用户请求中间过程
> 2. 整体流程图
> 3. 返回：由 `View` 视图里面自己编写的
> 26. 中间件：全局处理
> 27. 边边角角的功能，让  `Django`  更好用
> 28. `manage.py`  =>  请求和响应的中心
> 29. `URLConf`  =>  对 `URL` 进行解析
> 30. `View`  =>  进来的是 `HttpRequest`，返回的是 `HttpReponse`
> 31. 请求和返回都经过中间件
> 32. 请求：`WSGIHandler`
> 33. 响应：`Views.py`
> 34. `Django` 请求的一个小的闭环



## 1.6. Django 源码分析之 model 模型的自增主键创建

### 1.6.1. 获取源代码

```powershell
git checkout 7b
```



### 1.6.2. 源代码学习

**7b\MyDjango\Douban\models.py**

> 1. 继承自  `models.Model`
> 2. 跟踪官方代码



**site-packages\django\db\models\base.py**

> 1. `L399`  `class Model(metaclass=ModelBase):`
> 2. 元类：创建自己的类的时候增加一些自己的功能
> 3. 当前文件  `L67`  `class ModelBase(type):`  返回一个新的类
> 4. 判断当前类是不是 `ModelBase` 本身
> 5. 生成一个空的类
> 6. `add_to_class` 往类添加属性  `_meta` 属性  `Options()`
> 7. `_prepare()`  准备
> 8. `opts = cls._meta`
> 9. `opts._prepare(cls)   _meta._prepare  Options._prepare(cls)`
> 10. `_meta` 是 `Options` 类的实例对象，所以调用的是 `django.db.models.options.py` 下的 `_prepare()` 方法
> 11. `L206` `_prepare()`  是 `Options` 这个类的方法
> 12. `L225` `self.pk` 是不是主键 判断主键字段有没有设置，如果没有设置取第一个关联的父类 `Field`
> 13. 自增字段  =>  自增主键
> 14. 增加 `id` 字段
> 15. 注册模型
> 16. 返回新的类



### 1.6.3. 本节总结

> 1. 模型
> 2. 自定义的模型类继承自  `models.Model`
>    - 不需要显式定义主键
>    - 自动拥有查询管理器对象
>    - 可以使用  `ORM API`  对数据库和表实现  `CRUD`  操作
> 3. 自动创建 `id` 主键
> 4. 查询：直接去使用内置的查询的命令，查询管理器绑定的命令 `CRUD`
> 5. 最有意思
> 6. 而且功能强大



## 1.7. Django 源码分析之 model 模型的查询管理器

### 1.7.1. 获取源代码

```powershell
git checkout 7b
```



### 1.7.2. 源代码学习

**6b\functions\p3_1closure.py**

> 1. 函数是一个对象，所以可以作为某个函数的返回结果
> 2. **直线公式**  `y=a*x+b`
> 3. 多个变量的定义：更方便
>    - `a` 和 `b` 都不变



**site-packages\django\db\models\manager.py**

> 1. `L165`  `class Manager(BaseManager.from_queryset(QuerySet)):`
> 2. 父类 `BaseManager`
> 3. `from_queryset()`  `@classmethod`  动态创建类
> 4. `L103`  `class_name = '%sFrom%s' % (cls.__name__, queryset_class.__name__)`
> 5. 格式化字符串，前后替换  `BaseManagerFromQuerySet`
> 6. 动态创建一个新的类
> 7. `_get_queryset_methods` `@classmethod`
> 8. 装饰器  =>  返回的是 `QuerySet` 对象实例
> 9. 遍历 `QuerySet` 的方法定义
> 10. `BaseManager` 同名方法会被跳过
> 11. 以 `_` 开头的方法会被跳过：内置方法不暴露给用户
> 12. `objects` 是 `BaseManager` 的实例
> 13. 修改  `object = NewManager()`
> 14. `from django.db.models import Manager`
> 15. `class NewManager(Manager):`



### 1.7.3. 本节总结

> 1. 查询管理器 `object`
> 2. 查询方法
> 3. `objects` 改名
> 4. 返回值 `QuerySet` 对象
> 5. `Manager` 继承自 `BaseManagerFromQuerySet` 类，拥有 `QuerySet` 的大部分方法，`get create filter` 等方法都来自 `QuerySet`



## 1.8. Django 源码分析之 template 模板的加载文件

### 1.8.1. 获取源代码

```powershell
git checkout 7b
```



### 1.8.2. 源代码学习

**7b\MyDjango\index\views.py**

> 1. `L30`  `return render(request, 'bookslist.html', locals())`
> 2. 跟踪官方代码



**site-packages\django\shortcuts.py**

> 1. `L31`  `def render(request, template_name, context=None, content_type=None, status=None, using=None):`
>    - `render` 定义过程
>    - `request`  请求
>    - `template_name`  模板文件名
> 2. `render_to_string()`  继续跟踪
> 3. 返回 `HttpResponse`



**site-packages\django\template\loader.py**

> 1. `L52`  `def render_to_string(template_name, context=None, request=None, using=None):`
> 2. `L61` `get_template()`  继续跟踪
> 3. 当前文件 `L5`  `def get_template(template_name, using=None):`
> 4. `engines`  模板解析引擎
>    - 在 `settings.py` 指定引擎
> 5. 当前文件 `L65`  `def _engine_list(using=None):`
> 6. 该方法返回后端列表，主要实现依赖于 `engines`，它是一个 `EngineHandler`
> 7. `L47`  `site-packages\django\template\__init__.py`
> 8. `L16`  `site-packages\django\template\utils.py`
> 9. 初始化方法
> 10. 装饰器 `@cached_property`
> 11. `templates`  是有序字典
> 12. 遍历模板后端配置
> 13. `get_template()`  `find_template()`
> 15. 真正处理 `Template()`
> 16. `template_dirs` 列表，返回元组：目录信息
> 17. `app_config.path`
> 18. `dirname`  =>  `templates`



### 1.8.3. 本节总结

> 1. `templates` 固定目录
> 2. `settings.py` 里面模板一系列配置
> 3. 非常长的调用路径
> 4. 实现了很多功能的组合
> 5. 遍历 `APP`
> 6. 找到 `settings.py`  配置文件
> 7. 加载这些格式
> 8. 找到引擎
> 9. 通过引擎处理渲染的文件
> 10. 第一个：怎么找到配置文件
> 11. 第二个：目录的拼接



## 1.9. Django 源码分析之 template 模板的渲染

### 1.9.1. 获取源代码

```powershell
git checkout 7b
```



### 1.9.2. 源代码学习

**base.py**

> 1. `Template`  实现上面的 `Template` 的核心
> 2. `source` 存储的是模板文件的内容
> 3. 核心：`compile_nodelist()`  对模板内容进行切割  `parser.parse()`
> 4. 两大类
>    - `TextNode()`  静态页面
>      - 返回字符串本身
>    - `VariableNode()`  可变节点  `{{% %}}`
> 5. 解析  `tokenize()`  四种类型
>    - 变量类型：开头为 `{{`
>    - 块类型：开头为 `{%`
>    - 注释类型：开头为 `{#`
>    - 其他类型：字符串字面值



### 1.9.3. 本节总结

> 1. 使用引擎对模板文件进行渲染  `render`
> 2. 把模板进行拆分：富文本
> 3. 将不同的类型进行分类：可变  /  标准文本
> 4. 可变的进行二次分类，再进行相应的处理，再进行合并
> 5. 大量的缓存装饰器，可以对静态的内容进行加速，提高效率
> 6. 代码：查看及追踪
> 7. 画图：函数的调用顺序
> 8. 关注某一功能，从头跟踪到结束
> 9. 再对每一条线进行梳理



## 1.10. Django Web 相关功能 - 管理界面

### 1.10.1. 获取源代码

```powershell
git checkout 8a
```



### 1.10.2. Django 管理员

- 管理界面的设计哲学

  - 管理后台是一项缺乏创造性和乏味的工作，`Django`  全自动地根据模型创建后台界面
  - 管理界面不是为了网站的访问者，而是为管理者准备的

- 创建管理员帐号

  ```powershell
  python manage.py createsuperuser
  Username (leave blank to use 'maqiang'): 
  Email address: maqiang626@qq.com
  Password: 
  Password (again):
  The password is too similar to the username.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  
  ```

  

### 1.10.3. 源代码学习

**8a\MyDjango\index\admin.py**

> 1. **此文件完全新建**  =>  增加模型
> 2. 导入  `from django.contrib import admin`
> 3. 导入  `from .models import Type, Name`
>    - 引入数据库对应的模型的类的名称
> 4. 注册模型  `admin.site.register(Type)`



### 1.10.4. 本节总结

> 1. 默认的后台模板
>    - 默认关闭  =>  `migrate`  导入数据库
>    - 适用中小型项目
>    - 大型项目完全自己开发
> 2. 全局设置项  `settings.py`
>    - `django.contrib.admin`  必须加载
>    - 检查  `DATABASES`  设置正确
> 3. 官方文档：第 `7` 部分
>    - 丰富样式
>    - 投票系统



## 1.11. Django Web 相关功能 - 表单

### 1.11.1. 获取源代码

```powershell
git checkout 8b
```



### 1.11.2. 默认表单标准书写格式

```html
<form action="result.html" method="post">
username:<input type="text" name="username" /><br>
password:<input type="password" name="password" /> <br>
<input type="submit" value="登录">
</form>

```



### 1.11.3. 源代码学习

**8b\MyDjango\index\templates\form1.html**

> 1. 标准表单填充展示
> 2. 使用  `Django` 生成  `HTML`  代码
> 3. `form.py`  类比  `model.py`  `view.py`
>    - 完全新建
>    - 建议单独分拆



**8b\MyDjango\index\form.py**

> 1. 使用  `form`  对象定义表单
> 2. 继承自  `forms.Form`



**8b\MyDjango\index\templates\form2.html**

> 1. 引入  `form`  变量
> 2. 经过  `view`  视图  `urls.py`
> 3. 引入  `LoginForm`
> 4. 同时支持 `GET`  `POST`  方式



**8b\MyDjango\index\form.py**

> 1. 使用  `form`  对象定义表单
> 2. 继承自  `forms.Form`



### 1.11.4. 本节总结

> 1. 提交的请求方式  =>  `POST`
>    - 存入数据库
> 3. 对数据进行校验：请求中间件
> 3. 统一  `Python`  风格
>    - 魔术方法
>    - 类的继承
> 6. 官方文档  =>  表单
> 7. 集成：自动化表单功能
> 8. 类似模型：`ORM`  转成  `SQL`  语句



## 1.12. Django Web 相关功能 - 表单 CSRF 防护

### 1.12.1. 获取源代码

```powershell
git checkout 8b
```



### 1.12.2. 源代码学习

**8b\MyDjango\index\templates\form2.html**

> 1. {% csrf_token %}
> 2. 隐含值  =>  进行匹配
> 3. 中间件 settings.py  默认打开 django.middleware.csrf.CsrfViewMiddleware
> 4. 只用作 POST 不防护 GET
> 5. GET 防止数据被窃取 使用 HTTPS 进行防护



**8b\MyDjango\index\views.py**

> 1. 特殊的防护
> 2. 对某些请求进行防护
> 3. 导入 csrf_exempt
> 4. 只保护指定的视图
> 5. 免除某一个视图不被保护
> 6. 单独去控制不同的表单
> 7. 网页数据通过前端 Ajax 方式进行提交  =>  也必须添加 `CSRF` 请求信息



### 1.12.3. 本节总结

> 1. 表单提交：403 Forbidden
> 2. CSRF  跨站请求攻击
> 3. 网站会被恶意利用
> 4. 泄露用户信息
> 5. 进行防护：POST 页面添加 csrf_token
> 6. CSRF  one click attack     session reading
> 7. web 安全防护  SQL 注入



## 1.13. Django Web 相关功能 - 用户管理认证

### 1.13.1. 获取源代码

```powershell
git checkout 8b
```



### 1.13.2. 源代码学习

**8b\MyDjango\index\views.py**

> 1. 验证  `POST`  请求
> 2. 表单实例化  =>  取表单信息
> 3. 校验合法性  `is_valid()`
> 4. 读取表单的返回值
> 5. 开始验证
> 6. 验证函数  `authenticate`
> 7. `login`  `logout`



### 1.13.3. 本节总结

> 1. 用户认证系统
>    - 用户名和密码的正确性的验证
>    - 用户名和密码的注册
>    - 持久化存储
>    - 密码加密
> 4. 重复性劳动很多
> 5. 验证成功之后  =>  `session` 连接会话
> 6. 请求中间件  =>  验证功能
> 7. 注册用户  python manage.py shell
> 6. from django.contrib.auth.models import  User
> 7. user = User.objects.create_user('maqiang', 'maqiang626@qq.com', 'maqiangpassword')
> 8. user
> 9. user.save()
> 10. 进入数据库进行查询
> 11. use db1
> 12. show tables;
> 13. select * from auth_user \G
> 14. from django.contrib.auth import authenticate
> 15. authenticate(username='maqiang', password='maqiangpassword')
> 16. 验证失败返回空



## 1.14. Django Web 相关功能 - 信号

### 1.14.1. 获取源代码

```powershell
git checkout 8b
```



### 1.14.2. 信号概念

- 发生事件，通知应用程序
- 支持若干信号发送者通知一组接收者
- 解耦



### 1.14.3. 内建信号

- 模型类信号
  - `pre_init`
  - `post_init`
  - `pre_save`
  - `post_save`
  - `pre_delete`
  - `post_delete`
- 管理类信号
  - `pre_migrate`
  - `post_migrate`
- 请求响应信号



### 1.14.4. 源代码学习

**8b\MyDjango\index\views.py**

> 1. 绑定程序相关功能和信号
> 2. 如下两种方式实现
> 3. **1** 通过  `connect`  方式
>    - 注册机制
>    - 回调函数
> 4. **2** 通过装饰器方式  `receiver`
>    - `import django.dispatch import receiver`
> 5. 整体执行流程
>    - 请求开始
>    - 中间件
>    - 请求完成



### 1.14.5. 本节总结

> 1. 高级功能：功能更底层，用起来更实用，使用几率少
>    - 信号和中间件
> 2. 多线程涉及信号：两个线程之间互相通知
> 3. 多个独立的程序对某一个事件感兴趣
> 4. 官方文档  =>  内建信号
> 5. 程序和信号进行关联



## 1.15. Django Web 相关功能 - 中间件

### 1.15.1. 获取源代码

```powershell
git checkout 8b
```



### 1.15.2. 中间件概念

- 全局改变输入或输出
  - 请求  `HttpRequest`
  - 返回  `HttpResponse`
  - 请求和返回都是通过  `view`  视图和它们进行交互
  - 请求和返回都有处理顺序  `settings.py`
- 轻量级的、低级的“插件”系统
- 对请求、响应处理的钩子框架
- 每一个功能单独写一个文件  `middleware.py`



### 1.15.3. 源代码学习

**settings.py**

> 1. `MIDDLEWARE`
> 2. 不要更改默认顺序
> 3. 自己写的功能根据实际需求进行顺序的添加或插入



**8b\MyDjango\index\middleware.py**

> 1. 没有  `response`  后面的中间件就接收不到响应的信息了
>    - `return response`
> 2. 默认参数



### 1.15.4. 本节总结

> 1. 系统标准的中间件
>    - `csrf`
>    - `auth`
>    - `session`
> 2. 中间件：全局过滤的系统，更偏向底层
> 3. 类似：`getattr` `setattr`
> 4. 请求和返回的时候进行拦截处理
> 5. 中间件和信号：灵活去控制  `Django`
>    - 防爬虫
>    - 防注入
>    - 安全防护
>    - 防攻击
>    - 防无效请求



## 1.16. Django 相关功能 - 生产环境部署

### 1.16.1. 获取源代码

```powershell
git checkout 8b
```



### 1.16.2. 本节总结

> 1. `WSGi`  协议  `WSGIHandler`
>
>    - `HTTPRequest`  模拟  `HTTP`
>
>    - 请求  `HTTP`  协议
>
> 2. 把模拟功能转成正式功能
>
>    - 通用方法：中间转换器
>    - 接收用户发起的 `HTTP` 请求，转成 `WSGI` 协议给 `Django`
>    - 解决多用户访问阻塞问题
>
> 3. 转换器
>
>    - `Apache`
>    - `Nginx`
>    - `gunicon`
>      - 效率高，超过 `Nginx`
>      - 使用简单
>
> 4. 安装 gunicorn pip install gunicorn
>
> 5. 在项目目录执行 gunicorn MyDjango.wsgi 启动新的进程进行监听
>
> 6. gunicorn --help
>
> 7. -b  指定绑定的 IP 和端口
>
> 8. -w  多少个worker
>
> 9. --access-logformat 请求日志
>
> 10. --error-logfile 错误日志
>
> 11. --log-level 日志级别 info debug
>
> 12. --access-logfile 请求日志保存位置
>



## 1.17. Django 相关功能 - celery 介绍

### 1.17.1. 获取源代码

```powershell
git checkout 9a
```



### 1.17.2. Celery 架构

- 分布式消息队列
- 异步任务
  - `Async Task`
- 定时任务
  - `Celery Beat`
- 消息中间件
- 回调程序
- 结果存储
  - `Redis`



### 1.17.3. 本节总结

> 1. `Django`  和其他软件结合
>    - 实现数据存储  `Django + MySQL`
>    - 企业化部署  `Django + gunicorn`
> 2. 增强功能
> 3. 定时运行的任务
> 4. 分布式消息队列
> 5. `Celery`  分布式消息队列
> 6. 生产者：异步任务  定时任务 Celery Beat
> 7. 回调程序提前注册好
> 8. 先安装 Redis
> 9. make
> 10. make install
> 11. 启动 redis-server ./redis.conf
> 12. 生成磁盘文件 dump.rdb
> 13. 1 运行方式：daemonize no
> 14. 2 bind 127.0.0.1
> 15. 3 requirepass 123456
> 16. 守护进程 daemonize no
> 17. bind 127.0.0.1
> 18. requirepass 123456
> 19. 启动 redis-server ./redis.conf
> 20. 生成磁盘文件 dump.rdb
> 21. 安装 Celery pip install celery
> 22. pip install redis==2.10.6 数据库驱动程序
> 23. pip install celery-with-redis
> 24. pip install django-celery
> 25. 保留的关键字 async
> 26. 修改 async kombu 目录 async 
> 27. grep -ir asynchronous ..
> 28. 准备前期环境



## 1.18. Django 相关功能 - celery 定时任务的实现

### 1.18.1. 获取源代码

```powershell
git checkout 9a
```



### 1.18.2. 本节总结

> 1. 通过 `admin` 管理界面可以管理定时任务
> 2. 把 `Celery` 集成到 `Django`
> 3. 新建 app  python manage.py startapp djcron
> 4. 添加 `app` 注册 app djcelery djcron
> 5. 迁移生成表 migrate
>    - 创建 djcelery 库和表
> 6. 配置 django 时区
> 7. crontab timedelta 
> 8. setup_loader()  初始化加载
> 9. 配置后端存储对应的路径 BROKER_URL
> 10. celery 设置时区会覆盖 Django 时区设置
> 11. 定时任务调度器 模板引擎
> 12. MyDjango 项目里建立 celery.py  可以不用做任何更改：初始化设置
> 13. 绝对路径的引入，后续使用 import 引入会忽略当前目录下的包
> 14. 写在最上面  `from __future__ import absolute_import`
> 15. 启动 生产者 消费者
> 16. celery -A MyDjango beat -l info
> 17. celery -A MyDjango worker -l info
> 18. 爬虫：定时爬取



## 1.19. Flask 上下文与信号

### 1.19.1. 获取源代码

```powershell
git checkout 9b
```



### 1.19.2. 源代码学习

**9b\hello.py**

> 1. 导入  from flask import Flask
> 2. pip install flask
> 3. app 实例化
> 4. 通过装饰器实现 MTV 请求 URL
> 5. export FLASK_APP=hello.py
> 6. flask run 自动去找 APP
> 7. 1



### 1.19.3. 本节总结

> 1. web 框架 Flask  微框架 wsgi Werkzeug jinjia
> 2. Django 更封闭 集成太重
> 3. MTV 设计模式不变
> 4. Flask  官方文档 快速上手
> 5. 差异：没有 request 关键字，通过上下文
> 6. pip install flask



## 1.20. Tornado 简介与其他常见网络框架对比

### 1.20.1. 获取源代码

```powershell
git checkout 9b
```



### 1.20.2. 本节总结

> 1. 底层 `IO` 库 `Tornado`
> 2. 同步
> 3. 异步：支持
> 4. web 服务端程序
> 5. 兼容性最好
> 6. gevent 代码好维护
> 7. twisted 稳定性最好 支持 TCP UDP
> 8. tornado 兼容性最好





# 2. 本周作业

## 作业说明

**使用 Django 的 Form、Auth 组件，实现用户登录和密码验证功能。**

**要求：**

1. 登录界面要求能够输入用户名、密码，且密码需大于 8 位。
2. 用户名、密码通过 Django 的 Auth 组件对数据库中预先存储的用户密码进行验证。
3. 如果登录失败提示用户密码错误，登录成功后跳转到首页（或其他非登录的页面）。



## 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week11/job/AuthProject





# 3. 学习总结

## 3.1. 收获

1. Django 源代码
2. URLConf
3. View
4. Model
5. Template



## 3.2. 问题及不足

1. Django 源代码博大精深
2. 周边插件



## 3.3. 改进

### 3.3.1. 深入学习

1. Django 整体源代码
2. 多积累实际经验



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

Django !!!

