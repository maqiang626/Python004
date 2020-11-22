# Week07-08 学习笔记 (2020.11.1 - 2020.11.22)



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
      <td>1. 类属性与对象属性 <br>
          2. 类的属性作用域 <br>
          3. 类方法描述器 <br>
          4. 静态方法描述器 <br>
          5. 描述器高级应用 __getattribute__ <br>
          6. 描述器高级应用 __getattr__ <br>
          7. 描述器原理 & 属性描述符 <br>
          8. 面向对象编程 - 继承 <br>
          9. solid 设计原则与设计模式 & 单例模式 <br>
          10. 工厂模式 <br>
          11. 元类 <br>
          12. mixin 模式</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-11-22 18:08</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>









# 第七、八周：面向对象编程


# 1. 课程内容知识点学习

## 1.1. 类属性与对象属性

### 1.1.1. 获取源代码

```powershell
git checkout 6a
```



### 1.1.2. 类的成员：属性

- 类属性
  - 类属性字段在内存中只保存一份
  - 多个引用：一份内存
  - 静态字段
- 对象属性
  - 对象属性在每个对象都保存一份
  - 不同作用域的时候使用
  - 类实例化
  - 普通字段



### 1.1.3. 源代码学习

**6a\NewClass\p2_class_property.py**

> 1. `self` 实例化本身  =>  约定俗成 (不建议修改)
>
> 2. 静态字段 `vs` 普通字段
>
> 3. 获取作用域已经定义的属性和方法  `__dict__`
>
> 4. `Human.__dict__`
>
>    ```python
>    mappingproxy({'__module__': '__main__', 'live': True, '__init__': <function Human.__init__ at 0x0000017656593678>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None})
>    
>    ```
>
> 5. `man.__dict__`
>
>    ```python
>    {'name': 'Adam'}
>    
>    ```
>
> 6. 区分静态字段和普通字段：通过 `__dict__` 查看
>
>    ```python
>    >>> Human.__dict__
>    mappingproxy({'__module__': '__main__', 'live': True, '__init__': <function Human.__init__ at 0x0000017656593678>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None})
>    >>> man.__dict__
>    {'name': 'Adam'}
>    >>> woman.__dict__
>    {'name': 'Eve'}
>    >>> man.name
>    'Adam'
>    >>> woman.name
>    'Eve'
>    >>> Human.name
>    Traceback (most recent call last):
>      File "<stdin>", line 1, in <module>
>    AttributeError: type object 'Human' has no attribute 'name'
>    
>    ```
>
> 7. 高级区分进行验证
>
>    ```python
>    >>> man.age = 36
>    >>> man.__dict__
>    {'name': 'Adam', 'age': 36}
>    >>> woman.__dict__
>    {'name': 'Eve'}
>    >>> man.live
>    True
>    >>> woman.live
>    True
>    >>> man.live = False
>    >>> man.__dict__
>    {'name': 'Adam', 'age': 36, 'live': False}
>    >>> man.live
>    False
>    >>> woman.live
>    True
>    >>> Human.live
>    True
>    >>> woman.__dict__
>    {'name': 'Eve'}
>    
>    ```
>
> 8. 每个实例化引用普通字段：每个实例占用不同的内存
>
>    ```python
>    >>> man.name
>    'Adam'
>    >>> woman.name
>    'Eve'
>    >>> man.name = 'maqiang'
>    >>> man.name
>    'maqiang'
>    >>> woman.name
>    'Eve'
>    >>> man
>    <__main__.Human object at 0x0000017656737308>
>    >>> woman
>    <__main__.Human object at 0x0000017656737D48>
>    
>    ```
>



**6a\NewClass\p1_class_obj.py**

> 1. 不同内存地址，两个不同对象
>
> 2. 相等：取值相等
>
>    ```python
>    >>> type(a)
>    <class '__main__.MyFirstClass'>
>    >>> type(b)
>    <class '__main__.MyFirstClass'>
>    
>    ```
>
> 3. 不相等：已经不是两个相同的对象
>
>    - 类比现实世界：是两块积木
>
>      ```python
>      >>> id(a)
>      1607768178312
>      >>> id(b)
>      1607768178440
>      >>> a.__class__()
>      <__main__.MyFirstClass object at 0x0000017656737F88>
>      >>> b.__class__()
>      <__main__.MyFirstClass object at 0x0000017656737FC8>
>      >>> a is b
>      False
>      >>>
>      
>      ```
>
> 4. 类也是对象
>
>    - 将类赋值
>
>    - 实例化 `d = c()`
>
>      ```python
>      >>> c = MyFirstClass
>      >>> d = c()
>      >>> d.__class__()
>      <__main__.MyFirstClass object at 0x000001765673A048>
>      
>      ```
>



### 1.1.4. 本节总结

> 1. 类：对象  =>  数据以及相关行为的集合
>    - 古典类  =>  `Python 2.2` 版本以前
>      - 类是单独的一个部分
>      - 基本的数据类型是另外的一个部分
>      - 这两个部分很难做父类之间的统一
>    - 新式类
>      - 继承自 `object`
>      - 和现有的数据类型同源  =>  是相同的一种类型
> 2. `Python`  =>  一切皆对象
> 3. 对象：类比现实世界
>    - 数字
>    - 字符串
>    - 列表
>    - 元组
>    - 字典
>    - 集合
>    - 有特定的功能
> 4. 类的两大成员
>    - 属性
>    - 方法



## 1.2. 类的属性作用域

### 1.2.1. 获取源代码

```powershell
git checkout 6a
```



### 1.2.2. 源代码学习

**6a\NewClass\p2_class_property.py**

> 1. 为类增加静态字段
>
>    ```python
>    >>> Human.newattr = 1
>    >>> Human.__dict__
>    mappingproxy({'__module__': '__main__', 'live': True, '__init__': <function Human.__init__ at 0x0000017656593678>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None, 'newattr': 1})
>    >>> dir(Human)
>    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'live', 'newattr']
>    >>>
>    
>    ```
>
> 2. 内置类型不能增加属性和方法
>
>    ```python
>    >>> setattr(list, 'newattr', 'value')
>    Traceback (most recent call last):
>      File "<stdin>", line 1, in <module>
>    TypeError: can't set attributes of built-in/extension type 'list'
>    >>>
>    
>    ```
>
> 3. 新式类：显示 `object` 类的所有子类  =>  树形结构  =>  对象
>
>    - `print( ().__class__.__bases__[0].__subclasses__() )`
>
>      ```python
>      >>> ()
>      ()
>      >>> type(())
>      <class 'tuple'>
>      >>> ().__class__
>      <class 'tuple'>
>      >>> ().__class__.__bases__
>      (<class 'object'>,)
>      >>> ().__class__.__bases__[0]
>      <class 'object'>
>      >>> ().__class__.__bases__[0].__subclasses__()
>      [<class 'type'>, <class 'weakref'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'int'>, <class 'bytearray'>, <class 'bytes'>, <class 'list'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'traceback'>, <class 'super'>, <class 'range'>, <class 'dict'>, <class 'dict_keys'>, <class 'dict_values'>, <class 'dict_items'>, <class 'odict_iterator'>, <class 'set'>, <class 'str'>, <class 'slice'>, <class 'staticmethod'>, <class 'complex'>, <class 'float'>, <class 'frozenset'>, <class 'property'>, <class 'managedbuffer'>, <class 'memoryview'>, <class 'tuple'>, <class 'enumerate'>, <class 'reversed'>, <class 'stderrprinter'>, <class 'code'>, <class 'frame'>, <class 'builtin_function_or_method'>, <class 'method'>, <class 'function'>, <class 'mappingproxy'>, <class
>      'generator'>, <class 'getset_descriptor'>, <class 'wrapper_descriptor'>, <class 'method-wrapper'>, <class 'ellipsis'>, <class 'member_descriptor'>, <class 'types.SimpleNamespace'>, <class 'PyCapsule'>, <class 'longrange_iterator'>, <class 'cell'>, <class 'instancemethod'>, <class 'classmethod_descriptor'>, <class 'method_descriptor'>, <class 'callable_iterator'>, <class 'iterator'>, <class 'coroutine'>, <class 'coroutine_wrapper'>, <class 'moduledef'>, <class 'module'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class 'Context'>, <class 'ContextVar'>, <class 'Token'>, <class 'Token.MISSING'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib._installed_safely'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class 'classmethod'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class 'zipimport.zipimporter'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'nt.ScandirIterator'>, <class 'nt.DirEntry'>, <class 'PyHKEY'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc_data'>, <class 'abc.ABC'>, <class 'dict_itemiterator'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'async_generator'>, <class 'collections.abc.Iterable'>, <class 'bytes_iterator'>, <class 'bytearray_iterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'range_iterator'>, <class 'set_iterator'>, <class 'str_iterator'>, <class 'tuple_iterator'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class 'MultibyteCodec'>, <class 'MultibyteIncrementalEncoder'>, <class 'MultibyteIncrementalDecoder'>, <class 'MultibyteStreamReader'>, <class 'MultibyteStreamWriter'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class 'importlib.abc.Finder'>, <class 'importlib.abc.Loader'>, <class 'importlib.abc.ResourceReader'>, <class 'operator.itemgetter'>, <class 'operator.attrgetter'>, <class 'operator.methodcaller'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class 'collections._Link'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.partialmethod'>, <class 'contextlib.ContextDecorator'>, <class 'contextlib._GeneratorContextManagerBase'>, <class 'contextlib._BaseExitStack'>, <class '__main__.Human'>, <class '__main__.MyFirstClass'>]
>      >>>
>      
>      ```
>



**6a\NewClass\p3_class_pro2.py**

> 1. 前面一个下划线：人为约定不可修改 `_age`
>
>    - 内部属性
>    - 中间值属性
>    - 参与中间运算
>
> 2. 前面两个下划线：私有属性 `__fly`
>
>    - **自动改名机制**
>
>      - 改名  =>  `_Human2__fly`
>
>    - 防止人为误修改
>
>    - 防止程序误调用
>
>    - 也可以手动访问修改后的名称：不建议
>
>    - 通过 `__dict__` 查看
>
>      ```python
>      >>> Human2.__dict__
>      mappingproxy({'__module__': '__main__', '_age': 0, '_Human2__fly': False, '__dict__': <attribute '__dict__' of 'Human2' objects>, '__weakref__': <attribute '__weakref__' of 'Human2' objects>, '__doc__': None})
>      >>>
>      
>      ```
>
> 3. 前后两个下划线：魔术方法 `__init__`  `__name__`
>
>    - 不会被自动改名
>    - 实现了类的特殊成员
>    - 不是所有的双下划线开头和结尾的方法都是魔术方法
>    - 魔术方法类似其他语言的接口
>



### 1.2.3. 本节总结

> 1. 工作中常见问题  =>  少踩坑
> 2. 给指定的类增加属性和方法 `setattr`



## 1.3. 类方法描述器

### 1.3.1. 获取源代码

```powershell
git checkout 6a
```



### 1.3.2. 类的成员：方法

- 普通方法
  - 至少一个 `self` 参数
  - 表示该方法的对象
  - `self` 不是 `Python` 的关键字
  - 实例方法
- 类方法
  - 至少一个 `cls` 参数
  - 表示该方法的类
  - 类的绑定
  - `cls` 不是 `Python` 的关键字
  - 语法糖 `@classmethod`
- 静态方法
  - 无参数
  - 由类调用
  - 不能由实例化对象调用
  - 不能调用类的属性和方法
  - 静态方法和类之间有一定的关联
  - 语法糖 `@staticmethod`
- 三种方法在内存中都归属于类



### 1.3.3. `__init__()`

- 魔术方法
- `__init__()`  方法所做的工作是在类的对象创建好之后进行变量的初始化
- `__init__()`  方法不需要显示返回，默认为 `None`，否则会在运行时抛出 `TypeError`
- 第一个参数 `self`



### 1.3.4. `self`

- 标识实例对象本身
- `self` 不是 `Python` 的关键字，可以将 `self` 替换成任何你喜欢的名称，如 `this`、`obj` 等，实际效果和 `self` 是一样的（不推荐）
- 在方法声明时，需要定义 `self` 作为第一个参数，调用方法的时候不用传入 `self`



### 1.3.5. 源代码学习

**6a\NewClass\p5_1classmethod.py**

> 1. **随着环境改变而改变** `__name__`
>
> 2. 调用方法  `cls().foo()`
>
> 3. 查找 `@classmethod` `@staticmethod`
>
>    - `import django`
>    - 学习官方文档相应功能使用
>
> 4. #########
>
> 5. 构造函数 `__new__()`  <=>  初始化函数 `__init__()`
>
> 6. 绑定方法
>
>    - `get_apple_to_eve` 是 `bound` 方法，查找顺序是先找 `s` 的 `__dict__` 是否有 `get_apple_to_eve`
>
>    - 如果没有，查找类 `Story`
>
>      ```python
>      >>> s = Story('anyone')
>      >>> print(s.get_apple_to_eve)
>      <bound method Story.get_apple_to_eve of <class '__main__.Story'>>
>      >>> print(s.get_apple_to_eve())
>      Python
>      >>> print(Story.get_apple_to_eve())
>      Python
>      >>> print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
>      <bound method Story.get_apple_to_eve of <class '__main__.Story'>>
>      >>> print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)
>      True
>      >>>
>      
>      ```
>
> 7. #########
>
> 8. 类实例化字符串变化时需要处理
>
>    - 解决方法1：修改 `__init__()`
>    - 解决方法2：增加 `__new__()` 构造函数
>    - 解决方法3：增加提前预处理函数
>
> 9. 由“解决方法3”铺垫至类方法 `@classmethod`
>
> 10. 类需要一系列构造函数的时候，使用类方法 `@classmethod`
>
>    - 构造函数有且只有一个，通常不满足需求
>
> 11. #########
>
> 12. 查找顺序：实例化对象  =>  类  =>  父类
>
>     - 类的继承  `MRO`
>



### 1.3.6. 本节总结

> 1. 定义函数名称：贴近实际含义
> 2. 类方法：构造函数
> 3. 两大应用场景 `@classmethod`
>    - 定义到父类  =>  子类引用
>    - 函数调用  =>  提前预处理



## 1.4. 静态方法描述器

### 1.4.1. 获取源代码

```powershell
git checkout 6a
```



### 1.4.2. 源代码学习

**6a\NewClass\p5_2staticmethod.py**

> 1. 根据外部的情况进行判断
> 2. 可以传入参数进行判断
>    - 在 `__init__()` 方法中进行判断传递
> 3. 查找 `Django` 中相应使用
>    - `uploadedfile.py`
>    - `base.py`



**6a\NewClass\p5_3staticVSclass.py**

> 1. 对比三种方法
> 2. 类三种方法语法形式



### 1.4.3. 本节总结

> 1. 静态方法：用法单一
> 2. 目的：已定义的函数和类产生一定的关系
> 3. 用途
>    - 做一些功能的转化
>    - 类型转换
>    - 增加复杂判断：多条语句组成
> 4. 类方法和静态方法区别：
>    - 调用的方式上
>    - 各自有各自的功能



## 1.5. 描述器高级应用 `__getattribute__`

### 1.5.1. 获取源代码

```powershell
git checkout 6a
```



### 1.5.2. 源代码学习

**6a\NewClass\p6_1getattribute.py**

> 1. 类  =>  实例化
> 2. 对实例属性进行修改
> 3. 对实例属性查询
> 4. 删除实例属性 `del`  =>  查询  =>  异常  `AtttributeError`
> 5. `__getattribute__()`  覆盖系统自带的同名方法  =>  拦截



**6a\NewClass\p6_2getattribute.py**

> 1. `return super().__getattribute__(item)`
>    - 存在的属性返回取值
>    - 不存在的属性返回 `AttributeError`
> 2. 为什么使用 `super()` 不使用 `self` ?
>    - `super()`  =>  当前的实例所在的类的父类
>    - 类的继承
>    - 使用 `self` 会自己调用自己造成死循环



**6a\NewClass\p6_3getattribute.py**

> 1. 捕获异常
>    - 实例属性注册到 `__dict__`
>    - 赋默认值
> 3. 特定属性进行捕获拦截
> 4. 动态语言特色：截取  =>  修改



### 1.5.3. 本节总结

> 1. 类的实例的属性描述符
>    - 读取
>    - 赋值
>    - 删除
> 2. 对**实例**获取属性这一行为进行操作  =>  获取拦截
>    - `__getattribute__()`
>      - 对所有属性的访问都会调用该方法
>    - `__getattr__()`
>      - 适用于未定义的属性
> 3. :warning: 对**类**获取属性则无法进行操作
> 4. 中间拦截操作  =>  `HOOK`



## 1.6. 描述器高级应用 `__getattr__`

### 1.6.1. 获取源代码

```powershell
git checkout 6a
```



### 1.6.2. 源代码学习

**6a\NewClass\p6_4getattr.py**

> 1. 重写 `__getattr__`
>    - 对于不存在的属性：返回默认值
> 3. `h1.__dict__`  =>  仍然只显示已经存在的属性
>    - `{'age': 18}`



**6a\NewClass\p6_5getattr.py**

> 1. 对指定属性进行处理
> 2. 不存在的属性 `self.item = item`
>    - 返回 `None`



**6a\NewClass\p6_6both_define.py**

> 1. 两个同时存在：功能重复
> 2. 执行顺序：`__getattribute__`  >  `__getattr__`  >  `__dict__`



### 1.6.3. 本节总结

> 1. 拦截：属性不在实例 `__dict__`
> 2. `__getattribute__` 总会被调用  =>  会造成一定的性能损耗
> 3. `__getattr__`  =>  `__dict__` 没有属性
>    - 使用 `hasattr` 进行判断，即使返回 `True`  =>  使用 `dir` 依然看不到已经存在属性
>    - 很多内置的方法进行判断，可能会出现不一致的情况
>    - **深入原理了解透彻**



## 1.7. 描述器原理 & 属性描述符

### 1.7.1. 获取源代码

```powershell
git checkout 6a
```



### 1.7.2. 属性描述符 property

- 描述器：实现特定协议(描述符)的类
- 属性描述符 `property`：底层方法的高级函数使用
  - `__get__`
  - `__set__`
  - `__delete__`
- `Django` 源代码：具体实现
  - `site-packages/django/db/models/base.py`



### 1.7.3. 源代码学习

**6a\NewClass\p7_1descraptor.py**

> 1. `__getattribute__` 底层原理是描述器
> 2. 展示描述器的访问流程：底层实现的工作原理
> 3. 读取变量 `__get__`
>    - 三个参数：固定值
>    - `self`
>    - `instance`
>    - `owner`
> 4. 设置属性值 `__set__`
>    - 三个参数：固定值
>    - `self`
>    - `instance`
>    - `value`
> 5. 删除属性值 `__delete__`
>    - 两个参数：固定值
>    - `self`
>    - `instance`
> 6. 对实例的属性读写和删除进行自定义操作
>    - 删除前进行提示操作



**6a\NewClass\p7_2descraptor.py**

> 1. 属性描述符 `@property` 
>    - 描述器的抽象
>      - `fget`
>      - `fset`
>      - `fdel`
>      - `doc`
>    - 将方法封装成属性
>      - 方法调用更复杂
>      - 属性：对象赋值取值
>    - 简化操作
> 2. 默认只有只读功能 `@property`
> 3. #########
> 4. 支持修改 `@gender2.setter`
> 5. 支持删除 `@gender2.deleter`
> 6. 另一种 `property` 写法
>    - `gender = property(get_, set_, del_, 'other property')`
> 7. 建议
>    - 被装饰函数建议使用相同的函数名称 `gender2`
>    - 使用 `setter` 并不能真正意义上实现无法写入，`gender` 被改名为 `_Article__gender`
> 8. `property`  =>   纯 `python` 实现



**6a\NewClass\p8_1demo.py**

> 1. `ORM(flask.ext.sqlalchemy)`
>    - 类似 `Django Model`
> 2. 一个表记录一个节点的心跳更新
> 3. 通过一个属性来获取节点是否可用，而不用写复杂的查询语句
>    - 当作属性 `is_active`
> 4. #########
> 5. 限制传入的类型和范围（整数，且满足18-65）
>    - `__get__`
>    - `__set__`
> 6. #########
> 7. 固定部分传递的参数



**6a\NewClass\p8_2models.py**

> 1. `flask`
> 2. 使用装饰器完成 `password` 的读取和写入功能分离
> 3. 读取密码  =>  返回 `None`
> 4. 设置密码  =>  `hash` 转换
> 5. 密码验证 `hash`



### 1.7.4. 本节总结

> 1. 更上层的应用 `__getattribute__` `__getattr__`
> 2. 描述器：实现特定协议的一组工具
> 3. `HTTP` 协议
>    - 实现协议的客户端：浏览器 / `requests`
>    - 实现协议的服务器：`Django`
> 4. 描述器协议底层：描述符
> 5. `property` 功能
>    - 把函数伪装成属性  =>  操作更简单；更优雅
>    - 读和写进行分离  =>  分权限进行控制
> 6. `property` 本质并不是函数，而是特殊类（实现了数据描述符的类）
>    - 如果一个对象同时定义了 `__get__()` 和 `__set__()` 方法，则称为数据描述符
>      - `property`
>    - 如果仅定义了 `__get__()` 方法，则称为非数据描述符
>      - `__getattribute__`
> 7. `property` 优点
>    - 代码更简洁，可读性、可维护性更强
>    - 更好的管理属性的访问
>    - 控制属性访问权限，提高数据安全性



## 1.8. 面向对象编程 - 继承

### 1.8.1. 获取源代码

```powershell
git checkout 6a
```



### 1.8.2. `OOP` 面向对象编程的特性

- 封装
  - 支持
  - 将内容封装到某处 (容器)
  - 从某处调用被封装的内容
- 继承
  - 支持单继承和多继承 / `MRO`
  - 基本继承
  - 多重继承
  - `mixin`
- 重载
  - 编程技巧
  - `Python` 无法在语法层面实现数据类型重载，需要在代码逻辑上实现
  - `Python` 可以实现参数个数重载
- 多态
  - 不支持
  - `Python` 不支持 `Java` 和 `C#` 这一类强类型语言中多态的写法
  - 动态语言  =>  `Python` 使用“鸭子类型”



### 1.8.3. object vs type

- `object` 和 `type` 都属于 `type` 类 `(class 'type')`

  - `type` 元类

  - `type` 太上皇

  - `object` 由 `type` 元类创建的

- `type` 类由 `type` 元类自身创建的

- `object` 的父类为空，没有继承任何类

- `type` 的父类为 `object` 类 `(class 'object')`

  - 对象由谁创建 `__class__`

  ```python
  >>> print('object', object.__class__, object.__bases__)
  object <class 'type'> ()
  >>> print('type', type.__class__, type.__bases__)
  type <class 'type'> (<class 'object'>,)
  >>>
  
  ```

- 类的创建关系

- 类的继承关系



### 1.8.4. 类的继承

- 单一继承：子类有一个父类
- 多重继承：父子孙
- 菱形继承（钻石继承）
- 继承机制 `MRO`
- `MRO` 的 `C3` 算法



### 1.8.5. 源代码学习

**6a\ObjectOriented\p1_inheritance.py**

> 1. 新式类 `(object)`
>
> 2. `gene` 有没有被继承  =>  没有被继承
>    
>    - 子类 `__init__` 重写了父类的方法
>    
>      ```python
>      >>> p1.gene
>      Traceback (most recent call last):
>        File "<stdin>", line 1, in <module>
>      AttributeError: 'Man' object has no attribute 'gene'
>      >>>
>      
>      ```
>    
> 3. `People` 的父类是谁  =>  `object`
>
> 4. 能否实现多重层级继承  =>  可以
>
> 5. 能否实现多个父类同时继承  =>  可以
>
>    - 自然语言  =>  类比现实世界
>      - 鼻子像妈妈
>      - 眼睛像爸爸



**6a\ObjectOriented\p2_inheritance.py**

> 1. `super().__init__(name)`
>    - 找到 `Man` 的父类 `People`，把类 `People` 的对象转换为类 `Man` 的对象
>    - `gene` 有没有被继承  =>  已经继承
>      - `super(Man, self).__init__()`
> 2. 多个父类同时继承  `class Son(Man, Woman):`
> 3. 新的问题：继承顺序



**6a\ObjectOriented\p3_diamond.py**

> 1. 菱形继承关系
>
> 2. 钻石继承
>
> 3. `class Subclass(LeftSubclass, RightSubclass):`
>
> 4. 深度优先：经典类的查找方式
>
> 5. 广度优先：新式类的查找方式
>
> 6. `MRO`
>
>    ```python
>    >>> print(Subclass.mro())
>    [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.RightSubclass'>, <class '__main__.BaseClass'>, <class 'object'>]
>    >>>
>    
>    ```
>
>    - 修改 `RightSubclass` 的父类为 `Object`
>
>      ```python
>      >>> print(Subclass.mro())
>      [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.BaseClass'>, <class '__main__.RightSubclass'>, <class 'object'>]
>      >>>
>      
>      ```
>
> 7. 手动梳理多继承：有向无环图 `DAG`
>
>    - 入度为 `0` 的节点
>    - 先从左边找
>    - 排除入度为 `0` 的节点
>    - 以此类推



**6a\ObjectOriented\p4_overload.py**

- [x] **没有实现重载功能**

```python
>>> inst.A()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: A() missing 2 required positional arguments: 'a' and 'b'
>>>

```



### 1.8.6. 本节总结

> 1. `OOP`
> 2. 新式类：全部继承自 `object`
> 3. `type` 类  =>  元类
> 4. 自己写的类模拟基本的数据类型



## 1.9. solid 设计原则与设计模式 & 单例模式

### 1.9.1. 获取源代码

```powershell
git checkout 6a
```



### 1.9.2. SOLID 设计原则

- 原则
  - 指导思想，不是法律规定必须遵守
  - 针对静态语言
- 单一职责原则
  - `Scrapy` 框架 (优秀)
    - 网站改版  =>  修改指定的类
    - `CSS` 更改
    - 保存内容格式更改 `JSON`
  - 大类拆成小类
  - 违反：维护复杂
- 开闭原则
  - 对扩展开放
    - 构造函数  `@classmethod`
    - 继承：子类重构
  - 对修改封闭
- 里氏替换原则
  - 继承：子类实现的方法完整的覆盖父类的方法
- 依赖倒置原则：静态语言的接口有关
  - 高层模块不应该依赖低层模块
  - 抽象  =>  程序解耦
- 接口分离原则：静态语言的接口有关
  - 接口隔离原则
  - 一个接口提供的方法刚好是我们所需要的这么多的属性
  - 接口过多：很多用不到
  - 接口过少：不好用



### 1.9.3. 单例模式

- 单例模式
  - 程序实例化只允许一个实例
- `__init__`  vs  `__new__`
  - `__new__` 是实例创建之前被调用，返回该实例对象，是静态方法
    - `@staticmethod`
    - `PEP`
  - `__init__` 是实例对象创建完成后被调用，是实例方法
    - 申请完内存
  - `__new__` 先被调用，`__init__` 后被调用
  - `__new__` 的返回值(实例)将传递给 `__init__` 方法的第一个参数，`__init__` 给这个实例设置相关参数



### 1.9.4. 源代码学习

**6a\DesignPattern\p1_single.py**

> 1. 第一种方式：装饰器实现单例模式
> 2. 使用字典的特性
>    - `instances['__main__.MyClass'] = MyClass()`
> 3. #########
> 4. 第二种方式：使用 `__new__` 方式实现单例模式
> 5. 针对单线程：没问题
> 6. 多线程：非线程安全的问题
>    - 加锁解决
>    - 创建实例之前加锁
>    - `finally` 释放锁
> 7. `Double Check` 保证并发环境中运行正确
> 8. #########
> 9. 第三种方式：`import`
> 10. `import` 机制是线程安全的



### 1.9.5. 本节总结

> 1. 一系列问题
>    - 类如何进行拆分
>    - 类里面的方法如何进行拆分
>      - 方法合并
>      - 方法抽象
>    - 动态特性  =>  `property`
> 2. 设计模式  =>  指导原则
>    - 设计模式用于解决普遍性问题
>    - 设计模式保证结构的完整性
> 3. 单例模式：三种方式实现



## 1.10. 工厂模式

### 1.10.1. 获取源代码

```powershell
git checkout 6a
```



### 1.10.2. 源代码学习

**6a\DesignPattern\p2_factory.py**

> 1. 设计原则
> 2. 简单工厂模式  ==  静态工厂模式
> 3. 三种角色
>    - 工厂角色
>      - 产生实例
>      - 判断输入参数
>    - 抽象产品角色
>      - 创建对象父类
>      - 提供公共接口
>    - 具体产品
>      - `Man`
>      - `Woman`
>      - 具体对象的实例
> 4. 类工厂模式：返回在函数内动态创建的类
>    - 定义一个空类  =>  为这个空类增加属性
>    - `setattr` 需要三个参数：对象  +  `key`  +  `value`
> 5. 类工厂应用
>    - `Django`
>    - `Scrapy`



### 1.10.3. 本节总结

> 1. 设计模式：`22` 个
>    - 造大桥的图纸
> 2. 工厂模式
>    - 简单工厂模式
>      - 解耦类
>    - 动态创建类  =>  动态语言特性



## 1.11. 元类

### 1.11.1. 获取源代码

```powershell
git checkout 6a
```



### 1.11.2. 元类概念

- 元类是创建类的类，是类的模板
- 元类是用来控制如何创建类的，正如类是创建对象的模板一样
- 元类的实例为类，正如类的实例为对象
- 创建元类的两种方法
  - `class`
  - `type`
    - `type`（类名，父类的元组（根据继承的需要，可以为空），包含属性的字典（名字和值））
- 元类可以在类刚开始创建的时候进行拦截，并增加相应的功能
- 函数：可调用对象
  - 使用类实现函数 `__call__`



### 1.11.3. 源代码学习

**6a\DesignPattern\p3_metaclass.py**

> 1. `type`
>
>    - 检查对象的类型
>    - 创建新的类
>
> 2. `type` 的三个参数：类名、父类的元组、类的成员
>
>    - `Foo = type('Foo', (), {'say_hi': hi})`
>
>      ```python
>      >>> Foo = type('Foo', (), {'say_hi': hi})
>      >>> type(Foo)
>      <class 'type'>
>      >>> foo = Foo
>      >>> type(foo)
>      <class 'type'>
>      >>> foo.say_hi
>      <function hi at 0x000001DAE211FEE8>
>      >>> foo.say_hi()
>      Hi metaclass
>      >>>
>      
>      ```
>
> 3. #########
>
> 4. 引入元类 `metaclass`
>
>    - 元类必须继承自 `type`
>    - 元类必须实现 `__new__` 方法
>    - **Python 3**  `metaclass=DelValue`
>    - **Python 2**  `__metaclass__ = DelValue`
>
> 5. 类在创建的时候增加相应的功能
>
> 6. 框架中使用元类情形较多



### 1.11.4. 本节总结

> 1. 类的工厂函数  =>  创建新的类
>    - 用起来复杂
>    - 不够灵活
> 2. 元类  =>  创建新的类
> 3. 元类  =>  创建类的类
> 4. 元  =>  超越原有的类
> 5. 元类 `type` 首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力



## 1.12. mixin 模式

### 1.12.1. 获取源代码

```powershell
git checkout 6a
```



### 1.12.2. 抽象基类

- 抽象基类（abstract base class, ABC）
  - 用来确保派生类实现了基类中的特定方法
- 使用抽象基类的好处
  - 避免继承错误，使类层次易于理解和维护
  - 无法实例化基类
  - 如果忘记在其中一个子类中实现接口方法，要尽早报错

```python
from abc import ABC


class MyABC(ABC):
    pass


MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

```



### 1.12.3. Mixin 模式

- 在程序运行过程中，重新定义类的继承，即动态继承
- 使用 `mixin` 好处
  - 可以在不修改任何源代码的情况下，对已有类进行扩展
  - 进行组件的划分
    - 不同的组件放在不同的类中
    - 使用的时候通过 `mixin` 进行组合



### 1.12.4. 源代码学习

**6a\DesignPattern\p4_abc.py**

> 1. `from abc import ABCMeta, abstractmethod`
>
> 2. 定义抽象类 `metaclass=ABCMeta`
>
> 3. 定义抽象方法 `@abstractmethod`
>
> 4. 子类必须完全实现抽象父类的全部方法
>
>    ```python
>    TypeError: Can't instantiate abstract class Concrete with abstract methods bar
>    
>    ```



**6a\DesignPattern\p5_1mixin.py**

> 1. 类的继承  =>  动态改变继承关系
> 2. 父类 `__bases__`
>    - 修改继承顺序  =>  修改运行的逻辑和功能
> 3. 根据 `MRO` 顺序进行调用



**6a\DesignPattern\p5_2mixin.py**

> 1. 代码：混合显示和日志的功能
> 2. 类的继承  =>  程序的运行流程
> 3. 根据 `MRO` 顺序进行调用
>    - 通过  `print`  进行调试显示
> 4. 复杂继承
> 5. 这样操作的意义 `!!!`



### 1.12.5. 本节总结

> 1. 抽象基类
> 2. 动态语言
>    - 类可以动态去加载
>    - 类型可以动态去改变
> 3. `Mixin`  类无法单独使用，必须和其他类混合使用，来加强其他类
> 4. `《Python GUI Programming with Tkinter》`





# 2. 本周作业

## 2.1. 作业说明

**背景：**在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

```python
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    
```

**具体要求：**

1. 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
2. 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
3. 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
4. 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。



## 2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week07%2B08/job



实现过程：

> 1. 分别定义四个类
> 2. 定义类的继承关系
> 3. 对于不能实例化的类定义为抽象基类
> 4. 使用属性描述符便捷化操作属性



代码说明：

> 1. `metaclass=ABCMeta`
> 2. `@abstractmethod`
> 3. `setattr(self, animal.__class__.__name__, True)`
> 4. `@property`
> 5. `super().__init__(kind, somatotype, disposition)`
> 6. `self.is_pet = not self._is_ferocious`



问题及解决方案：

> - [x] This error occurs when we use the membership test a in b, but the type of b does not support membership tests.
>   - The standard Python types which support membership tests are strings, lists, tuples, and dictionaries.





# 3. 学习总结

## 3.1. 收获

1. `OOP`
2. 类属性和对象属性
3. 属性作用域
4. 类方法
5. 静态方法
6. 描述器高级应用 `__getattribute__` `__getattr__`
7. 属性描述符  `@property`
8. 类的继承
9. 设计模式 `SOLID`
10. 单例模式
11. 工厂模式
12. 元类
13. 抽象基类
14. `Mixin` 模式



## 3.2. 问题及不足

1. 魔术方法多
2. 设计模式的应用
3. `mixin` 应用



## 3.3. 改进

### 3.3.1. 深入学习

1. `OOP`
2. `class`
3. 装饰器
4. 设计模式
5. 结合成熟的框架学习面向对象编程



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

1. 面向对象编程思想
2. `Python` 高级语法和应用
3. `Python` 原理深入

