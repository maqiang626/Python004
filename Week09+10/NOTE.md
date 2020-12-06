# Week09-10 学习笔记 (2020.11.15 - 2020.12.6)



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
      <td>1. 变量的赋值 <br>
          2. 容器序列的深浅拷贝 <br>
          3. 字典与扩展内置数据类型 <br>
          4. 函数的调用 <br>
          5. 变量作用域 <br>
          6. 函数工具与高阶函数 <br>
          7. 闭包 <br>
          8. 装饰器介绍 <br>
          9. 被装饰函数带参数和返回值的处理 <br>
          10. Python 内置装饰器 <br>
          11. 类装饰器 <br>
          12. 官方文档中的装饰器代码阅读指南 <br>
          13. 对象协议与鸭子类型 <br>
          14. yield 语句 <br>
          15. 迭代器使用的注意事项 <br>
          16. yield 表达式 <br>
          17. 协程简介 <br>
          18. aiohttp 简介</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-12-06 22:10</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>










# 第九、十周：Python 高阶语法

# 1. 课程内容知识点学习

## 1.1. 变量的赋值

### 1.1.1. 获取源代码

```powershell
git checkout 6b
```



### 1.1.2. 数据类型划分：可变和不可变

- 可变和不可变：从使用内存的角度进行分类
- 可变数据类型 (动态)
  - 列表 `list`
  - 字典 `dict`
  - 内存地址不变
    - 内存内容发生变化
    - 内存地址扩充
- 不可变数据类型 (非动态 / 静态)
  - 整型 `int`
  - 浮点型 `float`
  - 字符串 `str`
  - 元组 `tuple`
  - 相同的对象  =>  只占一块内存
  - 改变值  =>  创建新的对象  =>  开辟新的内存空间
    - `GC`
- 从性能着手进行变量的实际定义



### 1.1.3. 源代码学习

**1 6b\datastruct\p1_1var.py**

> 1. 变量赋值
> 2. 判断值是否相等 `==`
> 3. 判断是不是同一个对象 `is`
>    - 内存空间是否相同
>    - 使用 `id` 查看
> 4. 三个变量指向了同一个内存地址
>



**2 6b\datastruct\p1_1var.py**

> 1. 变量连续赋值
>2. (不可变) 变量赋新值  =>  `id` 会变
> 



**3 6b\datastruct\p1_1var.py**

> 1. 列表赋值
> 2. 不同的操作方式产生不同的结果
>    - 增加
>    - 整个替换
>    - 里面的某个值进行替换
> 3. 可变类型，内存地址扩充



**4 6b\datastruct\p1_1var.py**

> 1. 列表赋值
> 2. 列表内容整体替换  =>  `False`
>    - 一组箱子
> 3. 引用 / 内存



**5 6b\datastruct\p1_1var.py**

> 1. 列表内容每个元素分别替换  =>  `True`
>    - 引用没变
> 2. 对变量传递的内容到底是什么？
> 3. `Scrapy` 返回内容
> 4. 一切皆对象
>    - 传递对象本身  =>  不可变数据类型
>    - 传递对象的引用  =>  可变数据类型
> 5. 类比：箱子  <=>  内存地址 (`malloc`)
>    - 便签  =>  变量



### 1.1.4. 本节总结

> 1. 非常简单但又不简单的一个概念
> 2. 简单  =>  变量赋值
> 3. 不简单  =>  `Python`  基本数据类型非常的丰富
>    - 赋值时一系列问题
>    - 连续赋值  `c = b = a`
>    - 更改类型当中的某些属性
>      - 类型是否会发生变化
>      - 指向这个类型的变量的名称是否会发生变化
> 4. 类型划分  =>  底层如何工作



## 1.2. 容器序列的深浅拷贝

### 1.2.1. 获取源代码

```powershell
git checkout 6b
```



### 1.2.2. 数据类型划分：序列和非序列

- 类型的定义进行分类：序列和非序列
- 序列
  - 容器序列：能存放不同类型的数据
    - `list`
    - `tuple`
    - `collections.deque`
  - 扁平序列：存放的是相同类型的数据
    - `str`  统一识别为一个一个的字符
    - `bytes`
    - `bytearray`
    - `memoryview`
    - `array.array`
  - 可变序列
    - `list`
    - `bytearray`
    - `array.array`
    - `collections.deque`
    - `memoryview`
  - 不可变序列
    - `tuple`
    - `str`
    - `bytes`
- 非序列
  - `dict`
    - `hash`
- 拷贝：复写纸
- 可变类型存在深拷贝、浅拷贝问题
- 不可变类型（数字、字符串、元组）没有拷贝问题



### 1.2.3. 源代码学习

**1 6b\datastruct\p2_copy.py**

> 1. 容器序列的拷贝问题  =>  对象的引用问题
>2. 非容器序列不存在拷贝问题
> 3. `list` 产生新的列表
>    - 两份内存地址
> 4. 切片操作产生新的列表  `[:]`
> 5. 嵌套对象  =>  内存地址扩充  `append`
> 



**2 6b\datastruct\p2_copy.py**

> 1. 导入 `import copy`
>
> 2. 深浅拷贝
> 
>   - 浅拷贝 `copy.copy`
>      - 拷贝对象的引用
>   - 深拷贝 `copy.deepcopy`
>      - 拷贝对象值  =>  新的内存
>
>    ```python
> assert new_list4 == new_list5  # True
> assert new_list4 is new_list5  # False AssertionError
> 
> AssertionError
>   
>    ```
>



### 1.2.4. 本节总结

> 1. 深浅拷贝
>    - 只对容器序列有效
>    - 非容器序列无效
>    - 非序列也无效
> 2. 序列：容器序列
>    - 变量的修改
>    - 变量的赋值
> 3. `Python`  传的一切都是对象
>    - 对象本身
>    - 对象的引用  =>  容器



## 1.3. 字典与扩展内置数据类型

### 1.3.1. 获取源代码

```powershell
git checkout 6b
```



### 1.3.2. collections

- 使用 `collections` 扩展内置数据类型
  - 标准库
- `collections`  提供了加强版的数据类型
  - `namedtuple`  带命名的元组
  - `deque`  双向队列
  - `Counter`  计数器
  - ...



### 1.3.3. 源代码学习

**1 6b\datastruct\p3_collections.py**

> 1. 导入 `from collections import namedtuple`
>2. 带命名的元组
> 3. 数学运算
>



**2 6b\datastruct\p3_collections.py**

> 1. 导入 `from collections import Counter`
> 2. 计数器
> 3. 取得频率最高的前三个值  `cnt.most_common(3)`
> 4. `Counter` 具体算法实现



**3 6b\datastruct\p3_collections.py**

> 1. 导入  `from collections import deque`
> 2. 双向队列
> 3. 右侧添加  `append`
> 4. 左侧添加  `appendleft`



**6b\datastruct\p4_abc.py**

> 1. 计算欧式距离
> 2. 导入 `import numpy as np`
>    - 通过数学函数进行计算
> 3. 使用命名元组进行计算
>    - 三维
>    - `__sub__`
>      - **一看就不简单**
>      - 系统自带功能 `a - b`  =>  `a.__sub__(b)`
>      - 重构减法  =>  运算符重载
> 4. 鸭子类型和魔术方法



### 1.3.4. 本节总结

> 1. 字典与哈希
>    - 散列函数 `hash`
> 2. 哈希
>    - 映射关系
>    - 查找时间：线性时间
>    - 类比：取余数
>    - 哈希算法
> 3. 字典
>    - `key`
>      - 可以进行 `hash` (不可变类型)
>    - `value`



## 1.4. 函数的调用

### 1.4.1. 函数关注四个方面

- 调用：到底用的是函数的对象名称，还是函数运行起来拿到它的结果
- 作用域：变量同名不同空间
- 参数
- 返回值



### 1.4.2. 源代码学习

- [x] **自定义代码**

> 1. 传递函数的对象 `a = func`
>
> 2. 传递函数执行的结果 `b = func()`
>
>    ```python
>    def func():
>        pass
>    
>    
>    >>> func
>    <function func at 0x0000018F82203168>
>    >>> func()
>    >>> a = func
>    >>> b = func()
>    >>> a
>    <function func at 0x0000018F82203168>
>    >>> b
>    >>> type(a)
>    <class 'function'>
>    >>> type(b)
>    <class 'NoneType'>
>    
>    ```
>
> 3. 通过类产生函数 `__call__`
>
>    ```python
>    class Kls1(object):
>        def __call__(self):
>            return 2020
>    
>        
>    >>> inst1 = Kls1()
>    >>> inst1
>    <__main__.Kls1 object at 0x0000018F823A7D08>
>    >>> inst1()
>    2020
>    >>> type(inst1)
>    <class '__main__.Kls1'>
>    >>> type(inst1())
>    <class 'int'>
>    >>>
>    
>    ```
>
> 4. 类  <=>  函数
>
>    - 不带括号：类的对象
>    - 带括号：类进行实例化



### 1.4.3. 本节总结

> 1. 函数：可调用对象
>    - 定义 `def`
>    - 通过类产生函数
> 2. 不带括号：传递函数的对象
> 4. 带括号：函数执行



## 1.5. 变量作用域

### 1.5.1. 获取源代码

```powershell
git checkout 6b
```



### 1.5.2. 变量作用域

- 高级语言对变量的使用
  - 变量声明  =>  确定变量存在，准备分配内存空间
  - 定义类型  =>  分配内存空间大小
  - 初始化  =>  赋值并填充内存
  - 引用  =>  通过对象名称调用对象内存数据
- `Python`  和高级语言差别
  - 在模块、类、函数中定义，才有作用域的概念
  - `dict`  声明字典  =>  需要提前定义
  - 不需要指定类型
  - 不需要初始化
  - 好处：不用申请内存和释放
  - 坏处：传参可能传错参数
    - `Type Hint`  类型提示



### 1.5.3. LEGB

- `L-Local (function)`  函数内的命名空间
- `E-Enclosing function locals`  外部嵌套函数的命名空间
  - 闭包  `closure`
- `G-Global (module)`  函数定义所在模块 (文件) 的命名空间
- `B-Builtin (Python)`  `Python`  内置模块的命名空间
  - `import os`



### 1.5.4. 源代码学习

**1 6b\legb\p1_whatis_legb.py**

> 1. 函数外部使用函数内部定义的变量
> 2. `NameError`



**2 6b\legb\p1_whatis_legb.py**

> 1. 变量定义在外部；函数调用的下面
> 2. 函数内部无法使用
> 3. `NameError`



**LG 6b\legb\p1_whatis_legb.py**

> 1. 最外侧 `Global`
> 2. 最内部 `Local`
> 3. 中间 `Enclosing`
> 4. 逐步调试



**E 6b\legb\p1_whatis_legb.py**

> 1. 难理解
> 2. 闭包：和函数组合在一起



**B 6b\legb\p1_whatis_legb.py**

```python
>>> print (dir (__builtins__) )
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__',
'__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>>

```



**6b\legb\p2_why_legb.py**

> 1. 同名不同作用域的问题
>    - `LEGB`
>    - 避免这种编写方式
> 2. 查找顺序问题
>    - `L`  =>  `G`
>    - `G`  =>  `B`
>    - `L`  =>  `E`  =>  `G`  =>  `B`
> 3. 执行顺序



### 1.5.5. 本节总结

> 1. 变量作用域  ==  命名空间 (内存空间)
> 2. `return`  返回一个对象
> 3. 变量作用域：两个问题
>    - 同名不同空间问题
>    - 顺序问题
> 4. `LEGB`



## 1.6. 函数工具与高阶函数

### 1.6.1. 获取源代码

```powershell
git checkout 6b
```



### 1.6.2. 函数参数

- 必选参数
- 默认参数
- 可变参数
- 关键字参数
- 命名关键字参数
- 参数是函数  =>  高阶函数
- 位置参数
- 可变长参数 (动态参数)
  - 参数的对象类型
  - 字典  /  序列：列表、元组、字符串、数字



### 1.6.3. 偏函数

- `functools.partial`  返回一个可调用的  `partial`  对象
  - 固定函数的某些参数
- 使用方法：`partial(func, *args, **kwargs)`
- 注意事项
  - `func`  是必须参数
  - 至少需要一个  `args`  或  `kwargs`  参数
- 应用场景
  - `Django` `URLConf`  =>  `path`
  - 源代码分析



### 1.6.4. Lambda

- 有些函数比较简单  =>  封装成 `Lambda` 表达式
- `Lambda`  表达式
  
  - 匿名函数
  
    ```python
    k = lambda x: x+1
    print(k(1))
    
    ```
- `Lambda`  只是表达式，不是所有的函数逻辑都能封装进去
  - 赋值
  - 函数逻辑复杂则不适用
- `Lambda`  表达式后面只能有一个表达式
  - 实现简单函数的时候可以使用  `Lambda`  表达式替代
  - 使用高阶函数的时候一般使用  `Lambda`  表达式



### 1.6.5. 高阶函数

- 高阶函数定义
  - 参数是函数
  - 返回值是函数
- 常见的高阶函数
  - `map`
  - `reduce`
    - `functools`  包
  - `filter`
  - `apply`  =>  `Python 2.3`  被移除
- 推导式和生成器表达式可以替代  `map`  和  `filter`  函数



### 1.6.6. 源代码学习

**6b\functions\p1_args.py**

> 1. `*args`  序列参数
>    - 元组
> 2. `**kwargs`  关键字参数
>    - 优先获取
>    - 剩下的给可变长参数
> 3. 内部传递参数：有顺序
> 4. 类的继承和元类



**6b\functions\p2_lambda.py**

> 1. 高阶函数转换为  `lambda`
> 2. `k = lambda x:x+1`  ==   `def k(x): return x+1`



**6b\functions\p4_highorderfunc.py**

> 1. 高阶函数
>
> 2. 映射 `map`  =>  把后面的值依次用前面的函数进行处理
>
>    - `<map object at 0x000001E6017B7248>`
>
>    - **map(函数, 序列)**
>
>      - 将序列中每个值传入函数，处理完成返回为 `map` 对象
>
>    - 取一个值  `next`
>
>    - 取全部值  `list`
>
>      - 再去取值返回空  `[]`
>
>    - 迭代器的工作方式
>
>    - 推导式 `[square(x) for x in range(10)]`
>
>      ```python
>      >>> dir(m)
>      ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>      >>>
>      
>      ```
>
> 3. `reduce`
>
>    - 导入 `from functools import reduce`
>    - 把右侧的参数两两操作 (根据左边的函数定义)
>
> 4. 过滤 `filter`
>
>    - **filter(函数, 序列)**
>      - 将序列中每个值传入函数，符合函数条件的返回为 `filter` 对象
>    - 返回迭代器
>
> 5. 偏函数
>
>    - 导入  `import functools`
>    - 固定函数的某一个或某几个参数
>      - 对原有函数的封装
>    - 不能和原有函数同名  =>  否则会覆盖原有函数
>    - 系统自带的计数器功能  `itertools.count()`
>
> 6. 排序  `sorted`



### 1.6.7. 本节总结

> 1. 函数的参数  =>  和外部交互
> 2. 高阶函数：函数的参数也是函数
>    - 函数式编程
> 3. 官方文档  `functools`  `itertools`



## 1.7. 闭包

### 1.7.1. 获取源代码

```powershell
git checkout 6b
```



### 1.7.2. 函数的返回值

- 返回的关键字
  - `return`
    - 返回一个对象；返回给函数的调用方；或者是自己的父级的函数
    - 返回一个函数对象：变量继续调用
    - 把类返回给一个变量
  - `yield`  迭代器
- 返回的对象
  - 可调用对象  =>  闭包 (装饰器)



### 1.7.3. 闭包定义

- 内部函数对外部函数作用域里变量的引用 (非全局变量) 则称内部函数为闭包
  - 变量  =>  自由变量
- 闭包：函数里面又定义了函数



### 1.7.4. 源代码学习

**6b\functions\p3_1closure.py**

> 1. 函数是一个对象，所以可以作为某个函数的返回结果
> 2. **直线公式**  `y=a*x+b`
> 3. 多个变量的定义：更方便
>    - `a` 和 `b` 都不变



**6b\functions\p3_2closure.py**

> 1. 继续在前例的基础上  =>  `b` 变化
> 2. 闭包变量定义



**6b\functions\p3_3closure.py**

> 1. 函数继续进化
>
> 2. `LEGB`
>
>    - 作用域
>    - 顺序
>
> 3. 放到里面不受外面 `Global` 影响
>
>    ```python
>    # 编译后函数体保存的局部变量
>    print(my_line.__code__.co_varnames)
>    ('x',)
>    
>    # 编译后函数体保存的自由变量
>    print(my_line.__code__.co_freevars)
>    ('b',)
>    
>    # 自由变量真正的值
>    print(my_line.__closure__[0].cell_contents)
>    10
>    
>    ```
>
> 4. 函数有哪些属性
>
>    ```python
>    >>> func_magic = dir(func)
>    >>> func_magic
>    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>    >>>
>    
>    ```
>
> 5. 常规对象有哪些属性 (类的实例化)
>
>    ```python
>    >>> obj_magic = dir(obj)
>    >>> obj_magic
>    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>    >>>
>    
>    ```
>
> 6. 比较函数和对象的默认属性
>
>    ```python
>    >>> set(func_magic) - set(obj_magic)
>    {'__call__', '__qualname__', '__globals__', '__name__', '__code__', '__defaults__', '__kwdefaults__', '__annotations__', '__get__', '__closure__'}
>    >>>
>    
>    ```



**6b\functions\p3_4closure.py**

> 1. 第 `4` 个版本：闭包的进化
> 2. 可变：`a` `b`
> 3. 分别固定每条线
> 4. 函数外部的变量可以提前定义



**6b\functions\p3_5closure.py**

> 1. 第 `5` 个版本
> 2. 提前定义 `Global` 变量
> 3. `LEGB`



**6b\functions\p3_6closure.py**

> 1. 每次访问自增 `1`
> 2. 内部函数对外部函数作用域里变量的引用 (非全局变量) 则称内部函数为闭包
> 3. `nolocal`  访问外部函数的局部变量
> 4. 两个计数器分别不受影响



### 1.7.5. 本节总结

> 1. 闭包：函数里面又定义了函数
>    - 外部的函数和内部的函数不太相关
>      - 外部的函数用作某些功能的初次定义 (对功能做修改和装饰)
>      - 内部函数来去运行  =>  得到结果
>      - 对两部分功能解耦
>    -  设置模式：函数定义的时候已经设置好
>    - 引用或执行的时候不需要考虑模式
> 4. 闭包或装饰器：强调定义态而非运行态的状态
> 5. 闭包的基本用法



## 1.8. 装饰器介绍

### 1.8.1. 获取源代码

```powershell
git checkout 6c
```



### 1.8.2. 装饰器简介

- `PEP 318` 装饰器  /  `PEP 3129` 类装饰器
  - 为什么引入？
  - 解决了什么问题？
- 装饰器  =>  `@` 语法糖
- 增强而不改变原有函数
- 装饰器强调函数的定义态而不是运行态
- 装饰器两个功能
  - 让代码看起来更加的简明和优雅
  - 用起来非常灵活：为函数去添加想要的任何功能



### 1.8.3. 源代码学习

**6c\Decorate\p1_decorate.py**

> 1. 前置问题
>    - 函数对象
>    - 函数的执行
> 2. 装饰器在模块导入的时候自动运行



**6c\Decorate\p2_how_decorate.py**

> 1. 装饰器应用场景举例
> 2. `flask`  装饰器
> 3. 绑定  `URLConf`
> 4. 包装内容：多个装饰器



### 1.8.4. 本节总结

> 1. 装饰器：一种设计模式
>    - 用来增强 `Java` 语言函数的功能
>    - 让 `Python` 函数更加的强大
> 2. 装饰器：闭包实现
> 3. `target`  表示函数
> 4. `target()`  表示函数执行
> 5. `new=func`  体现一切皆对象，函数也可以被当做对象进行赋值
> 6. 装饰器起到修饰被装饰函数的作用



## 1.9. 被装饰函数带参数和返回值的处理

### 1.9.1. 获取源代码

```powershell
git checkout 6c
```



### 1.9.2. 被装饰函数

- 被装饰函数带参数
- 被装饰函数带不定长参数
- 被装饰函数带返回值



### 1.9.3. 源代码学习

**6c\Decorate\p3_funcion_args.py**

> 1. 被装饰函数带参数
> 2. **变变变**   `__name__`
> 3. 函数已经被替换成了装饰器的内部函数
> 4. 当你的函数带了两个参数的时候，装饰器内部也要带两个参数，才能接收参数；并且把参数传递给原函数
> 5. 被装饰函数带不定长参数 `*args` `**kwargs`
> 6. 被装饰函数带返回值
>    - 装饰器内部返回一个对象
>    - 上面或下面增加自己的功能，不用修改原有函数本身
> 7. 编写装饰器的通用的框架  =>  **掌握**



**6c\Decorate\p4_decorate_args.py**

> 1. 装饰器带参数
> 2. 外侧再去套一层函数：共 `3` 层
>    - 执行：`3` 个括号
> 3. 装饰器堆叠
>    - 有顺序
> 4. 无限多的装饰器进行修饰



### 1.9.4. 本节总结

> 1. 被装饰函数带参数和返回值
> 2. 装饰器带参数
> 3. 关注函数的四个方面：输入和输出



## 1.10. Python 内置装饰器

### 1.10.1. 获取源代码

```powershell
git checkout 6c
```



### 1.10.2. 源代码学习

**6c\Decorate\p5_wraps.py**

> 1. `@functools.wraps()`
> 2. 官方文档功能介绍
> 3. 保持函数不变
>    - 内层函数增加  `@warps(func)`
> 4. `flask`  使用  `@wraps()`  案例
> 5. 装饰器：权限验证、日志记录
> 6. `@wrapt`  逐渐淘汰  `@wrapt.decorator`



**6c\Decorate\p6_lru_cache.py**

> 1. `《fluent python》`
> 2. `@functools.lru_cache()`
>    - `functools.lru_cache(maxsize=128, typed=False)`  有两个可选参数
>    - `maxsize`  代表缓存的内存占用值，超过这个值之后，旧的结果就会被释放
>    - `typed`  若为  `True`，则会把不同的参数类型得到的结果分开保存
> 3. `LRU`  淘汰机制
> 4. 斐波那契数列



### 1.10.3. 本节总结

> 1. 内置  `functools`
>    - `functools.wraps()`  保证被替换的内部的函数还原回原始的函数
>    - `functools.lru_cache()`  多次调用使用缓存减少调用的次数
> 2. 重复造轮子



## 1.11. 类装饰器

### 1.11.1. 获取源代码

```powershell
git checkout 6c
```



### 1.11.2. 源代码学习

**6c\Decorate\p7_class_decorate.py**

> 1. 使用类做装饰器
> 2. 实现  `__call__`
>    - 当作外层函数
>    - 再增加内层函数
> 3. 类装饰器和函数装饰器区别：三点区别
>    - 引入  `__init__`  函数
>    - 外层函数  `__call__`
>    - 引入  `self`  作为第一个参数
> 4. 类计数器
>    - 属性记得加 **self** `self.num_calls += 1`
>    - 返回时记得加 **self** `return self._func(*args, **kargs)`



**6c\Decorate\p8_decorate_class.py**

> 1. 使用装饰器来装饰类
> 2. 对类中的某一个函数进行装饰
> 3. 装饰目的：重写  `display`



### 1.11.3. 本节总结

> 1. `Python 2.6`  开始添加类装饰器
> 2. 其他经常用在类装饰器的  `python`  自带装饰器
>    - `classmethod`
>    - `staticmethod`
>    - `property`
> 3. 使用类做装饰器
>    - 使用  `__call__`  把类模拟成函数
>    - 把类模拟成可调用的对象
>    - 对类中的某一个函数做装饰



## 1.12. 官方文档中的装饰器代码阅读指南

### 1.12.1. 获取源代码

```powershell
git checkout 6c
```



### 1.12.2. 源代码学习

**6c\Decorate\p9_other.py**

> 1. 官方文档相关示例
> 2. 向一个函数添加属性  `setattr`
> 3. #########
> 4. 函数参数观察器：方便调试
> 5. #########
> 6. `Python` `3.7`  引入  `Data Class`  =>   `PEP557`
> 7. 导入  `from dataclasses import dataclass`
> 8. 类型提示符  `Type Hint`
> 9. 不用在类中重新封装  `__eq__`
> 10. 存在的问题：`var_a` `var_b`  不能作为类属性访问；只能作为实例属性



### 1.12.3. 本节总结

> 1. 官方文档：案例
> 2. 新功能：可能存在问题
> 3. 学习读懂官方文档
> 4. `Python`  语言发展变化



## 1.13. 对象协议与鸭子类型

### 1.13.1. 获取源代码

```powershell
git checkout 6c
```



### 1.13.2. 对象协议

- 实现对象协议  =>  魔术方法
- 鸭子类型
  - 叫起来像鸭子
  - 走路像鸭子
- 容器类型协议
  - `__str__`  打印对象时，默认输出该方法的返回值
    - 在对象由  `print()`  函数输出时被隐式地调用
  - `__getitem__` `__setitem__` `__delitem__`  字典索引操作
  - `__iter__`  迭代器
  - `__call__`  可调用对象协议
- 比较大小的协议
  - `__eq__`  等于
  - `__ne__`  不等于
  - `__lt__`  小于
  - `__le__`  小于或等于
  - `__gt__`  大于
  - `__ge__`  大于或等于
- 描述符协议和属性交互协议
  - `__get__`
  - `__set__`
- 可哈希对象：字典  `key`
  - `__hash__`
- 上下文管理器  `with`
  - `__enter__()`
  - `__exit__()`



### 1.13.3. 源代码学习

**6c\DuckTyping\p1_duck.py**

> 1. `__str__`  实例化之后直接输出相应信息
> 2. 字典操作
>    - `__getitem__`  获取值
>    - `__setitem__`  设置值
>    - `__delitem__`  删除值
> 3. 迭代器  `__iter__`
> 4. 更直观的理解对象的描述以及相应的魔术方法



**6c\DuckTyping\p2_FormatString.py**

> 1. `__str__` `__repr__`
>    - `__str__` 
>      - 字符串形式
>      - 人为去看
>      - 正常输出
>    - `__repr__` 
>      - 返回原有内容
>      - 对象之间通信去调用
>      - 程序之间调用：遵从原有格式
> 2. 格式化输出字符串
>    - `%5.3f`  `% math.pi`   输出共五位，保留三位小数
>    - `{0}` `{1}`  `{other}`  位置替换和关键字参数替换
>      - `.format`  关键字
>    - `f-string`  最优用法



**6c\DuckTyping\p3_typehint.py**

> 1. 类型注解  `Type Hint`
>
> 2. 与鸭子类型相反的是静态类型，声明变量的时候就要指定类型，如果使用其他类型对变量赋值就会报错
>
> 3. 传递变量定义类型
>
> 4. 返回定义类型  `->`
>
>    ```python
>    def func(text: str, number: int) -> str:
>        return text * number
>    
>    
>    func('a', 5)
>    
>    
>    >>> func('a', 5)
>    'aaaaa'
>    >>> type(func('a', 5))
>    <class 'str'>
>    >>>
>    >>> func(4, 5)
>    20
>    >>> type(func(4, 5))
>    <class 'int'>
>    >>>
>    
>    ```
>
> 5. 只是类型注解，并不是强制要求



### 1.13.4. 本节总结

> 1. 尽量模拟成  `Python`  标准的数据类型
>    - 开发者：越写越简单
>    - 使用者：越用越简单
>    - 越学越简单
> 2. 简单和高效的开发
>    - 实现相应的魔术方法
> 3. 鸭子类型



## 1.14. yield 语句

### 1.14.1. 获取源代码

```powershell
git checkout 7a
```



### 1.14.2. 生成器

- 在函数中使用  `yield`  关键字，可以实现生成器
- 生成器可以让函数返回可迭代对象
- `yield`  和  `return` 不同
  - `return`  返回后，函数状态终止
    - 返回全部值
  - `yield`  保持函数的执行状态，返回后，函数回到之前保存的状态继续执行
- 函数被  `yield`  会暂停，局部变量也会被保存
- 迭代器终止时，会抛出  `StopIteration`  异常
- 生成器对象
  - `Iterables`  可迭代  =>  包含  `__getitem__()`  或  `__iter__()`  方法的容器对象
    - `for in`
  - `Iterator`    迭代器  =>  包含  `next()`  和  `__iter__()`  方法
  - `Generator`  生成器  =>  包含  `yield`  语句的函数



### 1.14.3. 源代码学习

- [x] **自定义代码**

> 1. `yield`
>
>    ```python
>    >>> def func():
>    ...     yield 0
>    ...
>    >>> type(func)
>    <class 'function'>
>    >>> type(func())
>    <class 'generator'>
>    >>> func
>    <function func at 0x00000256337EFEE8>
>    >>> func()
>    <generator object func at 0x0000025631B81E48>
>    >>>
>    
>    ```
>
> 2. 列表推导式  =>  元组 (生成器)
>
> 3. 通过  `list()`  强制转换成列表
>
>    ```python
>    >>> [i for i in range(0, 11)]
>    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>    >>> (i for i in range(0, 11))
>    <generator object <genexpr> at 0x0000025631B81E48>
>    >>> list(i for i in range(0, 11))
>    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>    >>>
>    
>    ```
>
> 4. `StopIteration`
>
>    ```python
>    >>> gennumber = (i for i in range(0, 11))
>    >>> next(gennumber)
>    0
>    >>> next(gennumber)
>    1
>    >>> list(gennumber)
>    [2, 3, 4, 5, 6, 7, 8, 9, 10]
>    >>>
>    
>    ```
>
> 5. 可迭代  `__iter__`



**7a\Conroutine\p1_iter.py**

> 1. `hasattr`   检测：是否有相应的功能
>    - `setattr`  增加
> 2. 结论一：列表是可迭代对象，或称为可迭代  `iterable` ，不是迭代器  `iterator`
> 3. `__iter__`  方法是  `iter()`  函数所对应的魔法方法
> 4. `__next__`  方法是  `next()`  函数所对应的魔法方法
> 5. 结论二：生成器实现了完整的迭代器协议
> 6. 类实现完整的迭代器协议
>    - `__iter__`
>    - `__next__`
>      - `if`  /  `else`
> 7. 函数实现完整的迭代器协议
>    - 增加  `yield`  语句
>    - 只要一个函数的定义中出现了  `yield`  关键词，则此函数将不再是一个函数，而成为一个“生成器构造函数”，调用此构造函数即可产生一个生成器对象
> 8. `check iter`  **可作为通用方法**



### 1.14.4. 本节总结

> 1. `yield`  函数会暂停
> 2. 新的类型：生成器 / 迭代器



## 1.15. 迭代器使用的注意事项

### 1.15.1. 获取源代码

```powershell
git checkout 7a
```



### 1.15.2. 源代码学习

**7a\Conroutine\p2_infinite.py**

> 1. 导入  `import itertools`
> 2. `itertools`   三个常见无限迭代器
>    - 计数器  `itertools.count()`
>    - 循环遍历  `itertools.cycle()`
>    - 重复功能  `itertools.repeat()`
> 3. 有限迭代器  `itertools.chain()`
>    - 避免多次循环
> 4. `Python 3.3`  引入了  `yield from`
>    - `PEP 380`
>    - 替代内层循环：自动迭代



**7a\Conroutine\p3_destroy.py**

> 1. 迭代器有效性测试
> 2. 字典进行插入操作后，字典迭代器立即失效
>    - `RuntimeError`
> 3. 尾插入操作不会损坏指向当前元素的  `list`  迭代器，列表会自动变长
> 4. 迭代器一旦耗尽，永久损坏  =>  `StopIteration`
>    - 有别于 `for in` ：此种方式可以重复取



### 1.15.3. 本节总结

> 1. 类比  `C++`  迭代器
> 2. 迭代器将变量暂存到内存中  =>  并不会省内存
> 3. 迭代器主要作用是实现了一个叫迭代器这样的协议
> 4. 注意事项  =>  少踩坑



## 1.16. yield 表达式

### 1.16.1. 获取源代码

```powershell
git checkout 7a
```



### 1.16.2. 源代码学习

**7a\Conroutine\p4_yieldexp.py**

> 1. 传递值
> 2. 使用  `next`
>    - 暂停，将  `yield`  值返回给我们的调用的程序
>    - 进行输出
> 3. 使用  `send`
>    - 让你的暂停的东西恢复，并且把这个值传递给你  `yield`  左边变量进行赋值
>    - 进行输入
>    - 发送空值  `send(None)`  /  `next()`
> 4. 将程序分成两部分
>    - `yield`  语句和上面当作程序的上半部分
>    - 剩下的当作下半部分
> 5. `yield`  接收程序的输入



### 1.16.3. 本节总结

> 1. `yield from`  是表达式，对  `yield`  进行了扩展
> 2. `yield`  作为表达式，为变量传递参数
>    - 即可以输出
>    - 又可以输入
> 3. `yield`  可以暂停程序，通过不同的语句可以恢复  `yield`，遇到下一个  `yield`  继续暂停
>    - 可以手工控制  `yield`
> 4. `yield`  可以为变量赋值  =>  表达式
>    - 值必须通过外部传入，通过  `send`  传递一个非  `None`  的值，才能够进行接收
>    - 如果传递空值，则和执行  `next()`  这个功能是一样的
> 5. 通过  `yield`  =>  实现另外的一种循环模式
>    - 这种模式可以人为控制
>    - 遇到  `IO`  可以停下来去做其他的事情
> 6. 通过  `yield`  实现另一种工作模式  =>  协程



## 1.17. 协程简介

### 1.17.1. 获取源代码

```powershell
git checkout 7a
```



### 1.17.2. 协程和线程的区别

- [x] `yield`  vs  `threading`
- 协程是异步的，线程是同步的
  - `next()`  暂停  =>  恢复
- 协程是非抢占式的，线程是抢占式的
  - 线程抢占  `CPU`  =>  尽快完成
  - 协程调度到才去执行
- 线程是被动调度的，协程是主动调度的
  - 线程启动，如果遇到  `GIL`  锁，则停止，等待被调度
  - 直接  `next()`  /  `send()`  启动
- 协程可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
  - 标准生成器缺少输入
- 协程是用户级的任务调度，线程是内核级的任务调度
  - 协程：更轻量级
- 协程适用于  `IO`  密集型程序，不适用于  `CPU`  密集型程序的处理
  - `GIL`
  - 多进程适合  `CPU`  密集型



### 1.17.3. 异步编程

- `Python 3.5`  版本引入了  `await`  取代  `yield from`  方式
- `await`  接收的对象必须是  `awaitable`  对象
  - `await`  必须放到函数当中
  
  - 导入  `import asyncio`
    - 底层是事件循环
    - `Python 3.4`  引入事件循环机制
    - 注册  =>  回调
    - 主要解决的问题：网络服务当中，当我们去请求网络，等对方返回；等待的过程是网络  `IO`  最重要的一个瓶颈；通过事件循环，当有事件时，先进行注册；再响应
    
  - 函数必须使用  `async`  进行修饰
  
    ```python
    import asyncio
    
    
    async def py35_coro():
        await stuff()
    
    ```
- `awaitable`  对象定义了  `__await__()`  方法
- 事件循环：程序分配了一些事务或者分配了一些消息的编程框架
  
  - `A`  =>  `B`
- `awaitable`  对象有三类
  - 协程  `coroutine`
  - 任务  `Task`
  - 未来对象  `Future`



### 1.17.4. 源代码学习

**7a\Conroutine\p6_async_await.py**

> 1. 装饰器  `@asyncio.coroutine`
> 2. `Python 3.5`  增加  `async` `await`
> 3. 在协程中等待三秒  `await asyncio.sleep(3)`
> 4. `asyncio.run()`  运行最高层级的  `conroutine`



### 1.17.5. 本节总结

> 1. 协程调用过程
>    - 调用协程时，会被注册到  `ioloop`，返回  `coroutine`  对象
>    - 用 `ensure_future`  封装为  `Future`  对象
>      - 避免大量的回调
>    - 提交给  `ioloop`
> 2. `asyncio`  更偏向底层
> 3. 官方文档



## 1.18. aiohttp 简介

### 1.18.1. 获取源代码

```powershell
git checkout 7a
```



### 1.18.2. 源代码学习

**7a\Conroutine\p8_aiohttp2.py**

> 1. 服务端
> 2. 导入  `from aiohttp import web`
> 3. 返回速度快  `web.Response()`
> 4. 真正启动  `web.run_app()`
>    - 事件循环和事件注册
> 5. 压力测试



**7a\Conroutine\p7_aiohttp1.py**

> 1. 客户端
> 2. 获取  `session`  对象
> 3. 事件信息注册  `aiohttp.ClientSession()`
> 4. 初始化事件循环
> 5. 添加任务  =>  并没有真正执行
> 6. 真正执行  `loop.run_until_complete(task)`
> 7. 单个网页的处理



**7a\Conroutine\p9_mapaio.py**

> 1. 多个网页的处理
> 2. 封装对象
> 3. 双层  `map`  进行处理
> 4. 预先定义好将会怎样执行



**7a\Conroutine\p10_proc_con.py**

> 1. `web`  服务端
> 2. 协程和多进程进行配合
> 3. 统计总运行时间 / 统计每一个协程运行时间
> 4. 启动进程池
> 5. 通过异步的方式运行进程池  `p.apply_async()`
> 6. 关闭进程
> 7. 运行的每一个进程里面都跑了协程  `asyncio.run()`
> 8. `test`  修改为每个程序的运行
> 9. 遇到  `IO`  阻塞就切换做其他事情



### 1.18.3. 本节总结

> 1. `aiohttp`  异步的  `HTTP`  客户端和服务端
> 2. `asyncio`  具体应用  =>  `aiohttp`
> 3. 异步编程  =>  逻辑复杂
>    - 事件循环
>    - 开发难度高
> 4. 更高效：协程结合多进程
> 5. 多线程结合多进程





# 2. 本周作业

## 2.1. 作业一

### 2.1.1. 作业说明

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

- list
- tuple
- str
- dict
- collections.deque



### 2.1.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week09%2B10/job1



## 2.2. 作业二

### 2.2.1. 作业说明

 自定义一个 python 函数，实现 map() 函数的功能。



### 2.2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week09%2B10/job2



## 2.3. 作业三

### 2.3.1. 作业说明

 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。



### 2.3.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week09%2B10/job3





# 3. 学习总结

## 3.1. 收获

1. `OOP`
2. 深浅拷贝
3. 函数的调用
4. 函数的作用域 `LEGB`
5. 函数的参数
6. 函数的返回值
7. 闭包
8. 装饰器
9. 协程
10. `yield`  语句 / 表达式
11. `aiohttp`



## 3.2. 问题及不足

1. 协程
2. 异步编程



## 3.3. 改进

### 3.3.1. 深入学习

1. `OOP`
2. 装饰器
3. 异步编程



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

1. `Python` 高阶知识深入学习
2. 工作中实际应用

