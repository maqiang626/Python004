# Week03 学习笔记 (2020.10.5 - 2020.10.18)



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
      <td>1. Scrapy 并发参数优化原理 <br>
          2. 多进程：进程的创建 <br>
          3. 多进程：多进程程序调试技巧 <br>
          4. 多进程：使用队列实现进程间的通信 <br>
          5. 多进程：管道共享内存 <br>
          6. 多进程：锁机制解决资源抢占 <br>
          7. 多进程：进程池 <br>
          8. 多线程：创建线程 <br>
          9. 多线程：线程锁 <br>
          10. 多线程：队列 <br>
          11. 多线程：线程池 <br>
          12. 多线程：GIL 锁与多线程的性能瓶颈 <br>
          13. 迷你 Scrapy 项目实践</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-10-18 23:31</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>










# 1. 课程内容知识点学习

## 1.1. Scrapy 并发参数优化原理

### 1.1.1. 获取源代码

```powershell
git checkout 3c
```



### 1.1.2. Twisted

```ini
# Twisted 2020-10-06 07:35


Name: Twisted
Version: 20.3.0
Summary: An asynchronous networking framework written in Python
Home-page: https://twistedmatrix.com/
Author: Twisted Matrix Laboratories
Author-email: twisted-python@twistedmatrix.com
License: MIT
Location: e:\toolsinstalldir\python\python37\lib\site-packages
Requires: constantly, incremental, attrs, Automat, hyperlink, zope.interface, PyHamcrest
Required-by: Scrapy
```



### 1.1.3. 源代码学习

**3c\twisted_demo.py**

> 1. 模拟 `Twisted` 完整过程
> 2. response: 返回信息
>    - 可变长参数 `*args`
>    - 关键字参数 `**kwargs`
> 3. callback: 回调函数
> 4. `start`
>    - 代码进入部分
>    - `@defer.inlineCallbacks` 装饰器功能
>    - 不做真正处理：获取页面 -> response -> callback
> 5. stop: 循环结束
> 6. 异步处理：for in / 回调结果放入 list
> 7. 真正启动：defer 加入列表 / reactor.run() 真正开始启动，对接到事件循环当中
> 8. 异步操作流程
>    - 前面构建整个操作过程
>    - 后面进行异步连接，真正执行
> 9. `Twisted` 
>    - 一个进程里面操作
>    - 异步 `I/O` 框架
>    - 任务之间互相独立，用于大量 `I/O` 密集型操作
> 10. `Reactor Loop`
>     - 请求有返回，执行 `Callback`
>     - 请求没有返回，执行循环
> 11. 代码执行结果：2 个 Deferred (两个任务)
> 12. 图
>     - 左下角：start
>     - 右下角：reactor.run()
> 13. 异步编程
>     - 多任务的同步编程
>     - 底层的多进程和多线程的相关知识



### 1.1.4. 本节总结

> 1. 多任务模型分为同步模型和异步模型
>
> 2. Scrapy 使用的是 `Twisted` 模型
>
> 3. Scrapy 尽快采集数据，尽快入库
>
> 4. Scrapy 内部原理
>
>    - 比使用 requests 效率更高
>    - requests: 同步处理 / 单任务
>    - Scrapy: 异步处理 / 多任务
>
> 5. Scrapy 参数调优 `settings.py`
>
>    ```python
>    # Configure maximum concurrent requests performed by Scrapy (default: 16)
>    #CONCURRENT_REQUESTS = 32
>    
>    # Configure a delay for requests for the same website (default: 0)
>    # See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
>    # See also autothrottle settings and docs
>    #DOWNLOAD_DELAY = 3
>    
>    DOWNLOAD_DELAY = 3
>    
>    # The download delay setting will honor only one of:
>    #CONCURRENT_REQUESTS_PER_DOMAIN = 16
>    #CONCURRENT_REQUESTS_PER_IP = 16
>    ```
>
> 6. `CONCURRENT_REQUESTS` 优化
>
>    - 同时并发数
>    - 目标网站的性能承载
>    - 发起端自身的性能承载
>    - 也有可能改小
>
> 7. `DOWNLOAD_DELAY` 优化
>
>    - 等待 3 秒
>    - 下载延时
>    - 防止爬取过快被反爬
>
> 8. `CONCURRENT_REQUESTS_PER_DOMAIN` / `CONCURRENT_REQUESTS_PER_IP` 调优
>
>    - 控制 `Scrapy` 底层并行爬取
>    - 此参数开启则 `CONCURRENT_REQUESTS` 相应失效
>
> 9. `Scrapy` 异步模型结合多进程和多线程相关知识，深入理解



## 1.2. 多进程：进程的创建

### 1.2.1. 获取源代码

```powershell
git checkout 3c
```



### 1.2.2. 源代码学习

**3c\1进程\p1_firstproc.py**

os.fork()

- 直接派生一个新的进程
- 此操作只能在 Linux / Mac 运行，不能在 Windows 上运行
- C++ 编写，和操作系统重度关联
- AttributeError: module 'os' has no attribute 'fork'



**3c\1进程\p2_fork.py**

> 1. os.fork() 同上一份代码
> 2. 获取当前进程 PID `os.getpid()`
> 3. 获取父进程 PID `os.getppid()`
> 4. os.fork() 运行时，会有 2 个返回值
>    - 返回值为大于 0 时，此进程为父进程，且返回的数字为子进程的 `PID`
>    - 当返回值等于 0 时，此进程为子进程



**3c\1进程\p3_process.py**

> 1. 多进程 `from multiprocessing import Process`
> 2. 多进程调用 `Process(target=f, args=('john',))`
>    - 五个参数 `multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})`
>    - group：分组，很少使用 (进程组划分)
>    - **常用 target**：表示调用对象，传入方法的名字 (不带括号)
>      - 可调用对象 `f`
>      - 调用 `f()` / 返回调用结果进行传递
>    - name：别名，相当于给这个进程取一个名字；方便自己进行控制
>    - args：表示被调用对象的位置参数元组
>      - 比如 target 是函数 a，他有两个参数 m，n，那么 args 就传入 (m, n) 即可
>    - kwargs：表示调用对象的字典
> 3. 启动进程 `p.start()`
> 4. `p.join()`
>    - 父进程等待子进程结束，父进程再去结束
>    - `join([timeout])`
>      - 如果可选参数 `timeout` 是 `None` （默认值），则该方法将阻塞，直到调用 `join()` 方法的进程终止
>      - 如果 `timeout` 是一个正数，它最多会阻塞 `timeout` 秒
>      - 可以捕获异常 / 写入日志
>    - 如果进程终止或方法超时，则该方法返回 `None`
>    - 检查进程的 `exitcode` 以确定它是否终止
>    - 一个进程可以合并多次 (子进程再去合并)
>    - 进程无法并入自身，因为这会导致死锁
>    - 尝试在启动进程之前合并进程是错误的 (需要写在 `start()` 后面)



### 1.2.3. 本节总结

> 1. 多进程
>    - 同步
>    - 多任务
>    - 父子关系：父进程 / 子进程 / 子子进程
> 2. 多进程的创建方式和启动方式
>    - `os.fork()` 更底层 / 底层原理
>    - `multiprocessing.Process()` 更高层 / 已封装
> 3. `join()` 的用法



## 1.3. 多进程：多进程程序调试技巧

### 1.3.1. 获取源代码

```powershell
git checkout 3c
```



### 1.3.2. 源代码学习

**3c\1进程\p4_advfork.py**

> 1. 启动子进程 `p = Process(target=run)`
> 2. 父进程等待子进程结束 `p.join()`
> 3. 注释 `p.join()` 会影响父子进程执行顺序



**3c\1进程\p5_debug.py**

> 1. 多进程日常调试方法 `__name__`
> 2. 使用函数的方式创建子进程
> 3. `p.name` 进程名称
>    - 默认名称 `Process-1`
> 4. `multiprocessing.active_children()` 活动的子进程
> 5. `multiprocessing.cpu_count()` `CPU` 核心数 (等于子进程数量)
> 6. `print('-'*20)`



**3c\1进程\p6_class.py**

> 1. 通过类继承 `Process` 实现多进程
>    - 重写 `__init__` / 传递参数
>      - `super().__init()`
>    - 重写 `run` / 方法名固定 / 多进程具体执行方法
>    - 继承 `BaseProcess` (跟踪官方方法)
> 2. 当不给 Process 指定 target 时，会默认调用 Process 类里的 `run()` 方法



### 1.3.3. 本节总结

> 1. `DEBUG` 随时都需要掌握
> 2. 多进程和多线程调试更要注意
> 3. 不同进程之间内存空间不同，类比批处理和 `Shell`
> 4. 调试方法
>    - 过程中增加更多的 `print` 信息
>    - `time.sleep()`



## 1.4. 多进程：使用队列实现进程间的通信

### 1.4.1. 获取源代码

```powershell
git checkout 3c
```



### 1.4.2. 源代码学习

**3c\1进程\p7_var.py**

> 1. 父进程和子进程之间区别
>    - 内存空间不同 (堆栈信息)
>    - 父进程在创建子进程时对全局变量做了一个备份
>    - 父进程中的全局变量与子进程的全局变量完全是不同的两个变量
> 2. 在子进程中修改全局变量对父进程中的全局变量没有影响
>    - `global num`
> 3. 全局变量在多个进程中不能共享



**3c\1进程\p8_queue1.py**

> 1. `from multiprocessing import Process, Queue`
> 2. 队列的用法在多进程和多线程中类似
> 3. `Queue` 类是一个近似 `queue.Queue` 的克隆
> 4. `Queue` 队列实现父子进程通信
>    - 父进程创建队列，并传递给子进程
>    - 子进程负责写 `put()`
>    - 父进程负责读 `get()`
> 5. 设置队列最大值 `maxSize`
> 6. `put()` 往队列里面放数据
>    - `put` 多值 / 最大值 `maxSize` (最好设置最大存储值)
>    - `blocked` 设置阻塞状态
>      - `True` 队列已满，等待 `timeout` -> 抛出异常
>      - `False` -> 抛出异常 `Queue.Full`
>    - `timeout` 超时时间
>    - 两个人同时去写：加锁机制
> 7. `get()` 从队列里取数据
>    - `blocked` 控制阻塞或非阻塞
>      - `True` 队列为空，等待 `timeout` -> 抛出异常
>      - `False` 返回 `Queue.Empty`
>    - `timeout` 超时时间



**3c\1进程\p9_queue2.py**

> 1. 子进程负责读和写
> 2. 两个子进程之间进行通信
> 3. 父进程等待子进程结束
> 4. `pr.terminate()` 强制结束进程



### 1.4.3. 本节总结

> 1. 多进程通信方式：无法使用变量赋值 (不同内存堆栈)
>    - 队列 `Queue` (使用频率更高：查看源代码 / 基于管道，加了线程安全和使用功能)
>    - 管道 `Pipe` (更原始)
>    - 共享内存 `ShareMem`
> 2. 多进程引发问题：争抢资源
> 3. `multiprocessing` 支持进程之间的两种通信通道
>    - 父子进程
>    - 子进程之间
> 4. 队列：线程和进程安全的
> 5. 多线程使用队列类似
> 6. 队列 `FIFO`



## 1.5. 多进程：管道共享内存

### 1.5.1. 获取源代码

```powershell
git checkout 3c
```



### 1.5.2. 源代码学习

**3c\1进程\p10_pipe.py**

> 1. 导入 `from multiprocessing import Process, Pipe`
> 2. 返回的两个连接对象 `Pipe()` 表示管道的两端
> 3. 每个连接对象都有 `send()` 和 `recv()` 方法（相互之间的）
> 4. 如果两个进程（或线程）同时尝试读取或写入管道的同一端，则管道中的数据可能会损坏：管道更原始，底层技能知识
> 5. 同时使用管道的不同端的进程不存在损坏的风险



**3c\1进程\p11_sharemem.py**

> 1. 导入 `from multiprocessing import Process, Value, Array`
> 2. 多个进程使用同一块内存
> 3. 使用 `Value` 或 `Array` 将数据存储在共享内存映射中
> 4. 这里的 `Array` 和 `numpy` 中的不同，它只能是一维的，不能是多维的
> 5. 和 `Value` 一样，需要定义数据形式：像编译型语言
> 6. 子进程赋值，父进程读取
> 7. 参数是 `array` 模块使用的类型的 `typecode`
>    - `'d'` 表示双精度浮点数
>    - `'i'` 表示有符号整数
>    - `arr[:]`



### 1.5.3. 本节总结

> 1. `Pipe()` 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）
>    - 双工：左进右出 / 右进左出
>    - 吸管的两端
>    - 管道是队列的底层工具，了解即可
> 2. 在进行并发编程时，通常最好尽量避免使用共享状态
> 3. 共享对象是进程和线程安全的



## 1.6. 多进程：锁机制解决资源抢占

### 1.6.1. 获取源代码

```powershell
git checkout 3c
```



### 1.6.2. 源代码学习

**3c\1进程\p12_nolock.py**

> 1. 不加锁，多个进程抢占内存；最终结果与期望结果不一致 (每次都可能不一样)
> 2. `for _ in` 只循环次数，不使用变量
> 3. `mp.Value('i', 0)` 定义共享内存



**3c\1进程\p13_lock.py**

> 1. 定义一个进程锁 `mp.Lock()`
> 2. 获取锁 `l.acquire()`
> 3. 释放锁 `l.release()`
> 4. 进程锁的信息传入各个进程中
> 5. 每个进程按照抢到锁的顺序进行执行



### 1.6.3. 本节总结

> 1. 锁很重要，使用锁禁止避免资源抢占
>    - 进程不安全
>    - 线程不安全
>    - 锁保证资源的抢占问题
>    - 锁不保证进程执行的顺序问题
> 2. 多种锁类型



## 1.7. 多进程：进程池

### 1.7.1. 获取源代码

```powershell
git checkout 3c
```



### 1.7.2. 源代码学习

**3c\1进程\p15_pool.py**

> 1. 导入进程池 `from multiprocessing.pool import Pool`
>    - `Pool` 类表示一个工作进程池
> 2. 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
> 3. 创建进程，放入进程池统一管理 `p.apply_async()`
>    - `apply_async()` 异步运行
>    - `apply()` 同步运行；每次运行一个进程，顺序执行
> 4. 如果我们用的是进程池，在调用 `join()` 之前必须要先 `close()`
>    - `close()` 优雅的结束
> 5. 在 `close()` 之后不能再继续往进程池添加新的进程
> 6. 进程池对象调用 `join()`，会等待进程池中所有的子进程结束完毕再去结束父进程
> 7. `terminate()` 一旦运行到此步，不管任务是否完成，立即终止
> 8. 父进程等待并接收子进程的结果



**3c\1进程\p16_timeout.py**

> 1. 进程池超时
> 2. 使用 `with` 描述符
> 3. 增加关键字参数 `processes = 4`
> 4. 休眠 10 秒，取结果时只等了 1 秒；造成异常
>    - 爬虫逻辑
>    - 处理并获取异常：是否被反爬虫



**3c\1进程\p17_map.py**

> 1. `with Pool(processes=4) as pool`
> 2. `pool.map()`必须是一个参数 (多个参数转换为元组或列表)
>    - `map` 输出列表
>    - `imap` 输出迭代器
>      - `<multiprocessing.pool.IMapIterator object>`
>      - `next()` 获取
>      - 一种协议
>        - 不操作就不输出
>        - 返回一个对象
>    - 各有各的优点



**3c\1进程\p18_deadlock.py**

> 1. 死锁
> 2. 子进程已经关闭



### 1.7.3. 本节总结

> 1. 进程池方便日常高效操作
>    - 进程数量非常多
>    - 每一个进程会消耗一个逻辑的 `CPU`
>    - 进程启动的数量正好等于 `CPU` 核心数
>    - 进程池体现的并发的概念
> 2. 根据 `CPU` 核心数设置进程池数量
> 3. 注意 `join()` 函数放的位置，防止死锁
> 4. 灵活使用 `with` 描述符
> 5. 灵活使用 `map`，单进程并发



## 1.8. 多线程：创建线程

### 1.8.1. 获取源代码

```powershell
git checkout 3c
```



### 1.8.2. 源代码学习

**3c\2线程\p1_func.py**

> 1. 导入多线程 `import threading`
> 2. 通过函数创建多线程 `threading.Thread()`
> 3. 用法和多进程类似



**3c\2线程\p2_class.py**

> 1. 面向对象的方式
> 2. 通过类的继承创建多线程 `MyThread(threading.Thread)`
> 3. `super().__init__()`
> 4. `run(self)` 固定方法
> 5. 用法和多进程类似
> 6. 除了主进程，产生了 2 个新线程



**3c\2线程\p3_alive.py**

> 1. 对多线程进行跟踪调试
> 2. 判断当前线程存活状态 `thread1.is_alive()`
>    - `True` / `False`
>    - 根据状态做后续处理
> 3. 线程名称 `thread1.getName()`
>    - 默认线程名称 `Thread-1`
> 4. `thread1.join()`



### 1.8.3. 本节总结

> 1. 调用方 (发起方)
>    - 阻塞：得到调用结果之前，线程会被挂起 `requests`
>    - 非阻塞：不能立即得到结果，不会阻塞线程 `Scrapy`
> 2. 被调用方 (接收方)
>    - 同步：得到结果之前，调用不会返回
>    - 异步：请求发出后，调用立即返回，没有返回结果，通过回调函数得到实际结果
> 3. 多进程 / 多线程 / 协程
> 4. 非阻塞异步效率高：逻辑难以排错
> 5. 多进程和多线程配合 (非对立 / 由系统控制)
>    - 多进程提高效率
>    - 多线程方便通信
> 6. 协程：进程切换更轻量级 / 由用户把控
> 7. 并发和并行 `Coffee`
>    - `CPython` 多线程 -> 并发
>    - 多进程 -> 并行



## 1.9. 多线程：线程锁

### 1.9.1. 获取源代码

```powershell
git checkout 3c
```



### 1.9.2. 源代码学习

**3c\2线程\p4_nolock.py**

> 1. 不加锁
>2. 创建 10 个线程
> 3. 直接输出 10 次结果 `num value is 10`



**3c\2线程\p5_lock.py**

> 1. 引入 `mutex = threading.Lock()`
> 2. 获得锁 `mutex.acquire(1)`
> 3. 释放锁 `mutex.release()`
> 4. 和多进程使用类似
> 5. 在真正操作之前加锁，操作完成之后释放锁
> 6. 同时启动 5 个线程，先获得锁的线程先执行



**3c\2线程\p6_rlock.py**

> 1. `Lock` 普通锁不可嵌套
>2. `RLock` 普通锁可嵌套
> 3. `Lock` 嵌套会出现死锁
> 



**3c\2线程\p7_condition.py**

> 1. 高级锁：条件锁
>2. `c = threading.Condition()`
> 3. `conn.wait_for(condition)`  # 这个方法接受一个函数的返回值
>4. 和队列类似 (生产者消费者模式)



**3c\2线程\p8_semaphore.py**

> 1. 高级锁：信号量
> 2. `semaphore = threading.BoundedSemaphore(5)` 
>    - 最多允许5个线程同时运行
>    - 超过进行阻塞
> 3. `semaphore.acquire()`
> 4. `semaphore.release()`



**3c\2线程\p9_event.py**

> 1. 事件： 定义一个 `flag`，`set` 设置 `flag` 为 `True` ，`clear` 设置 `flag` 为 `False`
> 2. `event.clear()`  # 主动将状态设置为红灯
> 3. `event.set()`  # 主动将状态设置为绿灯
> 4. `e.wait()`
>    - 检测当前 `event` 是什么状态
>    - 如果是红灯，则阻塞
>    - 如果是绿灯则继续往下执行
>    - 默认是红灯



**3c\2线程\p10_timer.py**

> 1. 定时器： 指定 `n` 秒后执行
> 2. `t = Timer(1,hello)`  # 表示 `1` 秒后执行 `hello` 函数



### 1.9.3. 本节总结

> 1. 每个编程语言都会遇到：锁机制
> 2. 普通锁：`Lock` (使用最多)
> 3. 嵌套锁：`RLock`
> 4. 条件锁：该机制会使线程等待，只有满足某条件时，才释放 `n` 个线程
> 5. 条件锁的原理跟设计模式中的生产者／消费者（`Producer`/ `Consumer`）模式类似
> 6. 信号量：内部实现一个计数器，占用信号量的线程数超过指定值时阻塞
> 7. 高级锁的应用场景：结合实际需求



## 1.10. 多线程：队列

### 1.10.1. 获取源代码

```powershell
git checkout 3c
```



### 1.10.2. 源代码学习

**3c\2线程\p11_queue.py**

> 1. 导入 `import queue` / `q = queue.Queue(5)`
> 2. `q.task_done()`
>    - 每次从 `queue` 中 `get` 一个数据之后，当处理好相关问题，最后调用该方法
>    - 以提示 `q.join()` 是否停止阻塞，让线程继续执行或者退出
> 3. `q.qsize()`  # 队列中元素的个数，队列的大小
> 4. `q.empty()`  # 队列是否为空
> 5. `q.full()`  # 队列是否已满
> 6. 生产者和消费者示例
>    - 定义写入锁
>    - 条件变量锁
>    - `while 1` / `while True`
>    - `global writelock`
>    - 生产者：先判断队列是否已满，若满了，则等待资源 `self.con.wait()`
>    - 消费者：先判断队列是否为空，若为空，则等待资源 `self.con.wait()`
>    - 通知功能



**3c\2线程\p12_priorityQ.py**

> 1. 优先级队列
> 2. `q = queue.PriorityQueue()`
>    - 每个元素都是元组
>    - 数字越小优先级越高
>    - 同优先级先进先出
>    - `q.put((-2, "sleep"))`
> 3. `queue.LifoQueue` 后进先出队列 / 类似堆栈 (官方文档)
> 4. `q.deque` 双向队列 (使用少)



**3c\2线程\p13_downQ.py**

> 1. 下载队列：爬虫相关
> 2. 实现类似 `Scrapy` 功能：实现 `requests` 多线程下载；提升性能
> 3. 启动 `5` 个下载线程
> 4. 即使关掉终端程序依然运行 `t.setDaemon(True)`
> 5. 把网址放入队列进行下载



### 1.10.3. 本节总结

> 1. 多线程：变量可以共享
> 2. 多种队列形式
> 3. 类似多进程
> 4. 队列：线程安全
> 5. `Python` 哲学：以简洁为美



## 1.11. 多线程：线程池

### 1.11.1. 获取源代码

```powershell
git checkout 3c
```



### 1.11.2. 源代码学习

**3c\2线程\p14_pool.py**

> 1. 导入 `from multiprocessing.dummy import Pool as ThreadPool`
>    - `ThreadPool` 名字便于区分
> 2. 开启线程池 `pool = ThreadPool(4)`
> 3. 获取 `urls` 的结果
>    -  `results = pool.map(requests.get, urls)`
>    - `map` 逐一映射
> 4. 关闭线程池等待任务完成退出 `pool.close()`
> 5. `pool.join()`



**3c\2线程\p15_threadpoolExecutor.py**

> 1. 导入 `from concurrent.futures import ThreadPoolExecutor`
>    - `Python3.2` 中引入了 `concurrent.futures` 库
>    - 并行任务的高级封装
>    - 利用这个库可以非常方便的使用多线程、多进程
>    - 更关注业务
> 2. `with` 管理器 `with ThreadPoolExecutor(3) as executor`
> 3. `executor.submit(func, seed)`
>    - `submit` 参数原样传递到对象
>    - `map` 映射，将参数拆开传递
> 4. 命名参数 `max_workers=1`



**3c\2线程\p16_deadlock.py**

> 1. 同时并发两个线程 `ThreadPoolExecutor(max_workers=2)`
>
> 2. 互相等待：`a` 等待 `b` / `b` 同时等待 `a` / 造成死锁
>
>    ```python
>    executor = ThreadPoolExecutor(max_workers=2)
>    a = executor.submit(wait_on_b)
>    b = executor.submit(wait_on_a)
>    ```



### 1.11.3. 本节总结

> 1. 线程池类似进程池
> 3. 线程池：最大线程并发的一个限制
> 3. 死锁：线程间互相等待 (注意防范)



## 1.12. 多线程：GIL 锁与多线程的性能瓶颈

### 1.12.1. 获取源代码

```powershell
git checkout 3c
```



### 1.12.2. 源代码学习

**3c\2线程\p18_pvt.py**

> 1. 运行同样的任务，统计运行时间
> 2. 多核 / 多进程最快，说明在同时间运行了多个任务
> 3. 多线程的运行时间居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的（`GIL`）



### 1.12.3. 本节总结

> 1. `GIL` 锁：全局锁 (全局解释锁)
>    - 每一个进程只有一个 `GIL` 锁
>    - `CPython` 单独运行一个进程
>    - 拿到 `GIL` 锁才可以使用 `CPU`
>      - 多线程之间进行锁的抢夺
>    - 一旦遇到 `I/O` 操作(读写磁盘，读写网络数据包)，`GIL` 锁就会被释放
> 2. 创建多线程和多进程有很多相似的地方
> 3. 多线程和 `GIL` 锁
>    - 本质上同一时间运行的只有一个线程，多个线程之间交替运行
>    - 同时多线程切换会有性能开销
>    - 爬虫：`I/O` 密集型，`I/O` 频繁切换，多线程有优势
> 4. 多进程：进程上下文交互
> 5. 根据实际应用场景选择多线程或多进程



## 1.13. 迷你 Scrapy 项目实践

### 1.13.1. 获取源代码

```powershell
git checkout 3c
```



### 1.13.2. 源代码学习

**3c\miniScrapy.py**

> 1. 保存结果 `book.json`
> 2. 任务队列：存放网页的队列
> 3. 爬虫线程：接收队列
> 4. 解析线程：`XPath` / `json.dump`
> 5. 结束 `crawl` 线程 `t.join()`
> 6. 结束 `parse` 线程
> 7. 退出主线程 `output.close()`



### 1.13.3. 本节总结

> 1. 自己动手造轮子 `Scrapy`
>    - `Thread`
>    - `Queue`
>    - `requests`
>    - 综合运用
> 2. 多线程相关知识
>    - 深入理解 `Scrapy` 框架原理
>    - 了解底层原理 `Threading`





# 2. 本周作业

## 2.1. 作业一

### 2.1.1. 作业说明

由 Dijkstra  提出并解决的哲学家就餐问题是典型的同步问题。该问题描述的是五个哲学家共用一张圆桌（如下图所示），分别坐在五张椅子上，在圆桌上有五个盘子和五个叉子，他们的生活方式是交替的进行思考和进餐，思考时不能用餐，用餐时不能思考。平时，一个哲学家进行思考，饥饿时便试图用餐，只有在他同时拿到他的盘子左右两边的两个叉子时才能进餐。进餐完毕后，他会放下叉子继续思考（关于哲学家就餐问题更详细的描述，请参考本节的 PDF 附件，里面有维基百科中的具体描述）。

![image](https://github.com/maqiang626/Python004/blob/master/Week03/DiningPhilosophersProblem.png)



请写出代码来解决如上的哲学家就餐问题，要求代码返回“当每个哲学家分别需要进食 n 次”时这五位哲学家具体的行为记录（具体需要记录哪些行为，请参考下面的代码）。

```python
# 示例代码
import threading
class DiningPhilosophers:
   def __init__(self):
   pass
# philosopher 哲学家的编号。
# pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
# eat 表示吃面。
# putLeftFork 和 putRightFork 表示放下左边或右边的叉子。
   def wantsToEat(self,
      philosopher,
      pickLeftFork(),
      pickRightFork(),
      eat(),
      putLeftFork(),
      putRightFork())

```



**测试用例：**

- 输入：n = 1 （1<=n<=60，n 表示每个哲学家需要进餐的次数。）

**预期输出：**

- [[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]

**解释:**

输出列表中的每一个子列表描述了某个哲学家的具体行为，它的格式如下：
 output[i] = [a, b, c] (3 个整数)

- a 哲学家编号。
- b 指定叉子：{1 : 左边, 2 : 右边}.
- c 指定行为：{1 : 拿起, 2 : 放下, 3 : 吃面}。
   如 [4,2,1] 表示 4 号哲学家拿起了右边的叉子。所有自列表组合起来，就完整描述了“当每个哲学家分别需要进食 n 次”时这五位哲学家具体的行为记录。



### 2.1.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week03/job1



实现过程：

> 1. 根据题目要求，输入每个哲学家需要进餐的次数
> 2. 使用线程锁防止死锁
> 3. 使用多线程进行进餐操作
> 4. 当左边的叉子可用，拿起左边叉子
> 5. 当右边的叉子可用，拿起右边叉子
> 6. 吃面并延时
> 7. 放下右边的叉子
> 8. 放下左边的叉子
> 9. 重复



代码说明：

> 1. get_eat_num()
> 2. threading.RLock()
> 3. DiningPhilosophersThread(threading.Thread)



问题及解决方案：

> - [x] 哲学家就餐问题，首先感觉很难，没什么思路
>   - 网上搜索，借鉴其他人解法



## 2.2. 作业二 (选做)

### 2.2.1. 作业说明

**背景：** 在数据分析的完整流程中 (数据收集、存储、清洗、展示)，数据收集的多少对最终分析结果有着直接影响，因此需要对外网的数据进行收集并整理，用于支持后续的分析。

**要求：**改造基于 requests 爬虫（换成 Selenium），增加多线程功能，实现通过拉勾网，获取 北、上、广、深四地 Python 工程师的平均薪水待遇，并将获取结果存入数据库。

1. 基于 selenium 和多线程方式进行网站内容的爬取。
2. 获取北京、上海、广州、深圳四个地区，各地区 100 个 Python 工程师职位的职位名称和薪资水平。
3. 相同地区、相同职位及相同待遇的职位需去重。
4. 将获取的内容存入数据库中。

**选做：**

1. 使用图形库展示各地区 Python 工程师薪资分布情况，使用不同颜色代表该地区 Python 工程师薪资高低情况（建议使用 echart 或 matplotlib，具体图形库不限）。

**说明：**

1. 如果网页提示“操作太频繁”等提示，需清理 cookie ，重新获取 URL，降低频率或采用其他反爬虫方式解决。
2. 禁止爬取网站中的个人信息。



### 2.2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week03/job2



图形库展示各地区 Python 工程师薪资分布情况：

![image](https://github.com/maqiang626/Python004/blob/master/Week03/job2/plot_salary_2020-10-18T23-06-05.png)



实现过程：

> 1. 创建多线程进行网页内容的爬取
> 2. 创建多线程进行页面内容的解析
> 3. 将解析的具体内容存入数据库
> 4. 进行绘图：最低工资 / 平均工资 / 最高工资



代码说明：

> 1. CrawlJobThread(threading.Thread)
> 2. ParseJobThread(threading.Thread)
> 3. StoreDB(object)
> 4. plot_salary()



问题及解决方案：

> - [x] Message: element click intercepted: Element <span hidefocus="hidefocus" action="next" class="pager_next ">...</span> is not clickable at point (955, 816). Other element would receive the click: <div class="body-container showData">...</div>
>     (Session info: chrome=85.0.4183.121)
>   - browser.execute_script("arguments[0].click();", btn_next)
> - [x] pymysql.err.Error: Already closed
>   - finally: pymysql_connect.close()





# 3. 学习总结

## 3.1. 收获

1. Scrapy 更多收获：并发参数调优
2. 多进程相关知识
3. 多线程相关知识
4. 官方代码和自己写的代码，都需要不断 print 进行调试，过程中进行思考和学习



## 3.2. 问题及不足

1. 多进程在实际项目中的具体运用

2. 多线程在实际项目中的具体运用

3. 锁机制的应用场景

   

## 3.3. 改进

### 3.3.1. 深入学习

1. Scrapy 深入学习；框架图；回溯其官方代码
2. 多进程 / 多线程 / 协程 (暂未学习)



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 通过作业可以串通这个章节的整个知识结构



## 3.4. 感悟

1. 多进程和多线程，更深入理解了计算机运行的一些机制
2. 锁的运用情况有了一些初步了解
3. Scrapy 作为一个强大的框架，必须反复琢磨
4. 自己动手造轮子
5. 哲学家就餐问题，值得深入琢磨

