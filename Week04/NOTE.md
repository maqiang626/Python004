# Week04 学习笔记 (2020.10.12 - 2020.10.25)



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
      <td>1. pandas 简介 <br>
          2. pandas 基本数据类型 <br>
          3. pandas 数据导入 <br>
          4. pandas 数据预处理 <br>
          5. pandas 数据调整 <br>
          6. pandas 基本操作 <br>
          7. pandas 分组聚合 <br>
          8. pandas 多表拼接 <br>
          9. pandas 输出和绘图 <br>
          10. jieba 分词与提取关键词 <br>
          11. SnowNLP 情感倾向分析</td>
      <td>maqiang<br/>
          maqiang626@qq.com</td>
      <td>2020-10-25 20:10</td>
   </tr>
	<tr height=60px>
      <td></td>
      <td></td>  
      <td></td>
      <td></td>
   </tr>
</table>












# 1. 课程内容知识点学习

## 1.1. pandas 简介

### 1.1.1. 获取源代码

```powershell
git checkout 4a
```



### 1.1.2. 安装 **scikit-learn matplotlib** (第三方库)

```powershell
pip install scikit-learn
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn
Successfully installed joblib-0.17.0 scikit-learn-0.23.2 scipy-1.5.2 threadpoolctl-2.1.0


pip install matplotlib
Installing collected packages: kiwisolver, cycler, pyparsing, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.2.0 matplotlib-3.3.2 pyparsing-2.4.7

```



### 1.1.3. 源代码学习

**4a\1pandas\p1_dataset.py**

> 1. 测试数据集结合 `pandas` 进行练习
> 2. 引入数据集 `from sklearn import datasets`
> 3. 使用鸢尾花数据集进行测试 `datasets.load_iris()`
>    - 字典类型：四个特征 -> 每一个特征对应的种类
> 4. 划分训练集和测试集 `test_size=0.25`
>    - 生产数据需要先转换为 `x` `y`
> 5. **load_xxx** 各种数据集
>    - load_boston Boston 房屋价格 回归
>    - load_digits 手写体 分类
>    - load_iris  鸢尾花 分类聚类



**4a\1pandas\p2_pdfirst.py**

> 1. 处理数据：缺失 / 重复 / 特殊字符
>
> 2. 当前文件 `__file__`
>
>    ```python
>    pwd = os.path.dirname(os.path.realpath(__file__))
>    book = os.path.join(pwd, 'book_utf8.csv')
>    ```
>
> 3. 读取 `csv` 文件 `pd.read_csv()`
>
>    - 类型 `DataFrame`
>    - `Excel` 当中的表格
>    - 显示前面和结尾，中间以省略号显示
>    - 默认添加行号
>    - 默认将第一行设置为表头：导致统计结果少一行
>      - 增加列名 `df.columns = ['star', 'vote', 'shorts']`
>
> 4. `df` 支持切片：行筛选
>
> 5. 筛选标题为"还行"这一列 `df['还行']`
>
> 6. 显示特定的行列 `df.loc[1:3, ['star']]`
>
> 7. 筛选功能：后续**分词**使用
>
>    - `df['star'] == '力荐'`
>      - `True` / `False`
>    - `df[df['star'] == '力荐']`
>      - 显示 `True` 具体内容
>
> 8. 去除缺失数据 `dropna()`
>
> 9. 数据聚合 `df.groupby('star').sum()`
>
> 10. 高级函数 `map()`
>
>     - 创建新列：字典
>     - `df['new_star'] = df['star'].map(star_to_number)`
>     - 后续可根据新列进行数据筛选



### 1.1.4. 本节总结

> 1. 数据区别
>    - 内容和预期有区别
>    - 存在特殊字符：颜文字
>    - 数据的杂音 / 噪声
>    - 结构化的数据 / 样例数据 / 演示数据 / 测试数据 -> 适合学习
> 2. `pandas` 潘大师（厉害）
>    - 类比：`Python` 里面的 `Excel`
> 3. 数据收集 -> 数据清洗 -> 数据切分
> 4. 约定俗成缩写
>    - `pandas -> pd`
>    - `numpy -> np` 
>    - `matplotlib -> plt`
>    - 输出 `DataFrame -> df`



## 1.2. pandas 基本数据类型

### 1.2.1. 获取源代码

```powershell
git checkout 4a
```



### 1.2.2. 源代码学习

**4a\1pandas\p3_series.py**

> 1. 创建 `Series`
>    - 通过列表创建
>    - 自动创建索引
>    - `dtype: object`
> 2. 通过字典创建带索引的 `Series` == 通过关键字创建带索引的 `Series`
> 3. 获取全部索引 `s1.index`
> 4. 获取全部值 `s1.values` / 类型 `<class 'numpy.ndarray'>`
> 5. 转换为列表 `s1.values.tolist()`
>    - 操作方便
>    - 处理高效
> 6. 使用 `index` 会提升查询性能
>    - 如果 `index` 唯一，`pandas` 会使用哈希表优化，查询性能为 `O(1)`
>    - 如果 `index` 有序不唯一，`pandas` 会使用二分查找算法，查询性能为 `O(logn)`
>    - 如果 `index` 完全随机，每次查询都要扫全表，查询性能为 `O(n)`



**4a\1pandas\P4_dataframe.py**

> 1. 创建 `DataFrame`
>    - 列表
>    - 嵌套列表
>    - 自动创建行索引 `0 1 2 ...`
>    - 自动创建列索引 `0 1 2 ...`
> 2. 自定义列索引 `df2.columns`
> 3. 自定义行索引 `df2.index`
> 4. `df2.values` `<class 'numpy.ndarray'>`



### 1.2.3. 本节总结

> 1. `pandas` 两种数据类型
>    - `Series`
>      - `Excel` **一列**或者一行
>      - 自动加索引，默认 `0 1 2 ...`
>      - `index`
>      - `value`
>    - `DataFrame`
>      - `Excel` 多行或多列
>      - 行索引
>      - 列索引
> 2. 两种类型的各种用法
> 3. 两种类型的适用场合
> 4. 正则表达式：基本功
> 5. `pandas`
>    - 基于 `numpy`
>    - 对 `numpy` 做的一种封装



## 1.3. pandas 数据导入

### 1.3.1. 获取源代码

```powershell
git checkout 4a
```



### 1.3.2. 安装 **xlrd** (第三方库)

```powershell
# ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.


pip install xlrd
Installing collected packages: xlrd
Successfully installed xlrd-1.2.0

```



### 1.3.3. 源代码学习

**4a\1pandas\p5_importdata.py**

> 1. `pd.read_excel()`
>    - 读取的时候依赖第三方库 `xlrd`
>    - 导入 `Excel` 
>    - 空值显示 `NaN`
>    - 导入指定 `sheet`
>      - `pd.read_excel(r'1.xlsx', sheet_name=0)`
> 2. 其他类型：`read_csv()` / `pd.read_table()`
> 3. 从数据库导入：`pd.read_sql(sql, conn)`
>    - `Python` + `pandas` + `MySQL`
> 4. 显示前几行：`excel1.head(3)`
> 5. 行列数量：`excel1.shape`
>    - `(3, 4)`
> 6. 详细信息 `excel1.info()`
> 7. 显示更详细信息 `excel1.describe()`



### 1.3.4. 本节总结

> 1. “菜：买回来；看看是否新鲜”
> 2. `pandas` 支持各种数据导入
> 3. 有机结合 `pymysql`
> 4. 对导入的数据做各种查询操作
> 5. 对数据全貌进行分析
> 6. `pandas` 擅长：数据预处理 / 数据清洗



## 1.4. pandas 数据预处理

### 1.4.1. 获取源代码

```powershell
git checkout 4b
```



### 1.4.2. 源代码学习

**4b\1pandas\p6_pre.py**

> 1. 检验序列中是否存在缺失值
>    - `x.hasnans`
>      - 存在空值 `True`
> 2. 将缺失值填充为平均值 `x.fillna(value=x.mean())`
> 3. 用上一行填充 `df3.ffill()`
> 4. 用前一列填充 `df3.ffill(axis=1)`
> 5. 缺失值删除 `df3.dropna()` `df3.info()`
> 6. 填充缺失值 `df3.fillna('无')`
> 7. 重复值处理 `df3.drop_duplicates()`
>    - 完全重复



### 1.4.3. 本节总结

> 1. “摘菜和洗菜”
> 2. 对数据做各种预处理：尊重规律和特性；尊重原始数据
>    - 缺陷数据处理：缺失值处理
>      - 填补：反复爬取相关数据进行补全
>      - 通过非技术手段进行补全
>    - 不适用部分处理：重复值处理
>      - 时间不同内容相同
>      - 多个用户提交的信息一致：产品策略上进行处理
> 3. 针对 `Series` / `DataFrame` 两种类型的数据



## 1.5. pandas 数据调整

### 1.5.1. 获取源代码

```powershell
git checkout 4b
```



### 1.5.2. 源代码学习

**4b\1pandas\p7_adjust.py**

> 1. 多列选择使用列表 `df[['A', 'C']]`
> 2. `df.iloc[:, [0, 2]]`   # : 表示所有行，获得第 1 和第 3 列
> 3. 行选择：`df.loc[[0, 2]]`   # 选择第 1 行和第 3 行
> 4. `df.loc[0:2]`   # 选择第 1 行到第 3 行
> 5. 替换
>    - 指定列指定值
>    - 多对一替换
>    - 多对多替换
>    - 原有 `df` 不变，可以保存到新的 `df` 里面
> 6. 删除
>    - 删除指定列
>    - 删除指定行
>    - 删除特定行
> 7. 行列互换 `df.T` / `df.T.T`
> 8. 数据透视表
>    - 行列不等
>    - 展开 `df4.stack()`
>    - 反向展开 `df4.unstack()`
>    - 空白填充 `df4.stack().reset_index()` / 自动添加索引



### 1.5.3. 本节总结

> 1. “对菜的形状进行调整”
> 2. 数据各种调整操作：增删改查
>    - 数据格式
>    - 数据内容
> 3. 矩阵：行列互换



## 1.6. pandas 基本操作

### 1.6.1. 获取源代码

```powershell
git checkout 4b
```



### 1.6.2. 源代码学习

**4b\1pandas\p8_operate.py**

> 1. 空值
>    - `numpy -> NaN`
>    - `Python -> None`
> 2. 两列之间的加减乘除 `df['A'] + df['C']`
>    - 空值不参与计算
>    - 空值计算返回 `NaN`
>    - 大小比较计算：空值永远返回 `False`
>      - 需要进行数据的清洗和预处理
> 3. 非空值计数 `df.count()` / 空值不被统计



### 1.6.3. 本节总结

> 1. “开始炒菜”
> 2. 算数运算 / 比较运算
>    - 行与列之间的计算
>    - 列与列之间的计算
> 3. 各种求值：通过官方文档页面 (第三方库的官方网站)
>    - 求和 `sum()`
>    - 求均值 `mean()`
>    - 求最大值 `max()`
>    - 求最小值 `min()`
>    - 求中位数 `median()`
>    - 求众数 `mode()`
>    - 求方差 `var()`
>    - 求标准差 `std()`
> 4. 需要熟悉数学计算基本功能：需要时快速调取



## 1.7. pandas 分组聚合

### 1.7.1. 获取源代码

```powershell
git checkout 4b
```



### 1.7.2. 源代码学习

**4b\1pandas\p9_group.py**

> 1. 分组 `df2.groupby('type').groups`
> 2. 聚合后再计算 `df2.groupby('type').count()`
> 3. 聚合 `aggregate()`
>    - 不进行合并 `transform()`
> 4. 数据透视表 `pd.pivot_table()`
>    - 数据处理 `data`
>    - 行 `index`
>    - 列 `columns`
>    - 处理方式 `count`
>    - `reset_index()`
>    - 根据实际需求进行调整



### 1.7.3. 本节总结

> 1. “将菜装盘：美观”
> 2. `pandas` 特色：分组和聚合
> 3. `pandas` 分组功能类似 `sql` 分组功能
>    - `groupby`
> 4. `pandas` 数据透视表和 `Excel` 数据透视表功能类比



## 1.8. pandas 多表拼接

### 1.8.1. 获取源代码

```powershell
git checkout 4b
```



### 1.8.2. 源代码学习

**4b\1pandas\p10_multitable.py**

> 1. 多表拼接
>    - 一对一 `pd.merge(data1, data2)`
>      - 默认使用公共列进行拼接
>    - 多对一 `pd.merge(data3, data2, on='group')`
>      - 有多个公共列
>      - `on` 指定拼接列
>    - 多对多 `pd.merge(data3, data2)`
>      - 获取公共部分
> 2. 连接键类型，解决没有公共列问题
>    - `left_on` 左表列
>    - `right_on` 右表列
> 3. 不指明连接方式，默认都是内连接
>    - `on` 指定列
>    - `how` 连接方式



### 1.8.3. 本节总结

> 1. “菜：拼盘”
> 2. 多表拼接：类比 `sql` 多表连接方式 (数据库操作)
> 3. 各种连接
>    - 左连接 `left`
>    - 右连接 `right`
>    - 外连接 `outer`
>    - 内连接 `inner`
>    - `Python` 用法：纵向拼接 `concat()`
>      - 拼接成大表
>      - 工作中使用最多



## 1.9. pandas 输出和绘图

### 1.9.1. 获取源代码

```powershell
git checkout 4b
```



### 1.9.2. 安装 **seaborn** (第三方库)

```powershell
pip install seaborn
Installing collected packages: seaborn
Successfully installed seaborn-0.11.0

```



### 1.9.3. 源代码学习

**4b\1pandas\p11_output.py**

> 1. 导出 `Excel` 文件
>    - `df.to_excel()`
>      - 依赖第三方库 `xlwt`
>      - 导出文件名 `excel_writer()`
>    - 设置 `Sheet` 名称 `sheet_name = 'sheet1'`
>    - 设置索引
>      - 设置参数 `index=False` 就可以在导出时把这种索引去掉
>    - 设置要导出的列 `columns = ['col1','col2']`
>    - 设置编码格式 `enconding = 'utf-8'`
>    - 缺失值处理 `na_rep=0`
>    - 无穷值处理 `inf_rep=0`
> 2. 导出为 `.csv` 文件 `to_csv()`
> 3. `pkl` 文件 `to_pickle()`



**4b\1pandas\p12_plot.py**

> 1. 导入 `import matplotlib.pyplot as plt`
>    - 显示图形 `plt.show()`
> 2. 绘制散点图 `plt.scatter(df.index, df['A'])`
> 3. 美化 `plt` `sns.set_style('darkgrid')`



### 1.9.4. 本节总结

> 1. “菜：装盘 / 更美观：摆盘”
> 2. `pandas` 数据导出
>    - 转成字典 `to_dict()`
>      - `Python` 进行后续处理
>    - 文件保存
> 3. 导出 `pkl` 文件性能高
>    - 推荐
>    - 后续 `Python` 处理
> 4. 使用内置函数性能更高 `agg`
> 5. 使用 `plt` 绘图，可以设置各种参数：颜色 / 线条样式 / 线条宽度 / 点标记
> 6. `seaborn` 其实是在 `matplotlib` 的基础上进行了更高级的 `API` 封装，从而使绘图更容易、更美观
>    - `import seaborn as sns`



## 1.10. jieba 分词与提取关键词

### 1.10.1. 获取源代码

```powershell
git checkout 4c
```



### 1.10.2. 安装 **jieba** (第三方库)

```powershell
pip install jieba

Using legacy 'setup.py install' for jieba, since package 'wheel' is not installed.
Installing collected packages: jieba
    Running setup.py install for jieba ... done
Successfully installed jieba-0.42.1

```



### 1.10.3. 源代码学习

**4c\2jieba\p1_mode.py**

> 1. 导入 `import jieba`
> 2. 精确模式 `jieba.cut(string, cut_all=False)`
> 3. 全模式 `jieba.cut(string, cut_all=True)`
> 4. 启发式搜索算法 `Viterbi`
> 5. 搜索引擎模式 `jieba.cut_for_search()`



**4c\2jieba\p2_keyword.py**

> 1. 对给定文章进行关键词提取
>    - 提取词
>    - 判断权重值
> 2. 导入 `import jieba.analyse`
> 3. 基于 `TF-IDF` 算法进行关键词抽取
>    - 经典算法
>    - 算法相对更准确
> 4. 基于 `TextRank` 算法进行关键词抽取
> 5. `pprint` 模块提供了打印出任何 `Python` 数据结构的类和方法
>    - `pprint.pprint()`



**4c\2jieba\p3_stopword.py**

> 1. 解决问题：去除不想展示的关键词
> 2. `stop_words` 的文件格式是文本文件，每行一个词语
> 3. 设置停止词 `jieba.analyse.set_stop_words(stop_words)`
> 4. 使用 `pprint` 输出
>    - **TOP K**



**4c\2jieba\p4_dict.py**

> 1. 文本文件：三部分 (一行)
>    - 关键词
>    - 权重
>    - 词性
> 2. 自定义词典 `jieba.load_userdict()`
> 3. 动态添加词典 `jieba.add_word('极客大学')`
> 4. 动态删除词典 `jieba.del_word('自定义词')`
> 5. 关闭自动计算词频 `HMM=False`
>    - 防止错误分词
> 6. 调整分词并合并 `jieba.suggest_freq()`



### 1.10.4. 本节总结

> 1. 机器推荐
>    - 自然语言处理
>    - 语义分析
> 2. 分词
>    - 英语：默认每个单词以空格分隔
>    - 中文：一句话
> 3. `jieba`：默认是精确模式
> 4. 设置 `keyword`
> 5. 设置 `stopword`
> 6. 自定义词典：词性表



## 1.11. SnowNLP 情感倾向分析

### 1.11.1. 获取源代码

```powershell
git checkout 4c
```



### 1.11.2. 安装 **snownlp** (第三方库)

```powershell
pip install snownlp

Using legacy 'setup.py install' for snownlp, since package 'wheel' is not installed.
Installing collected packages: snownlp
    Running setup.py install for snownlp ... done
Successfully installed snownlp-0.12.3

```



### 1.11.3. 源代码学习

**4c\3nlp\p1_snownlp.py**

> 1. 导入 `from snownlp import SnowNLP`
> 2. 中文分词 `s.words`
> 3. 词性标注 (隐马尔可夫模型)
>    - 正向：趋近于 `1`
>    - 负向：趋近于 `0`
> 4. 情感分析（朴素贝叶斯分类器）
>    - `0 - 1`
> 5. 拼音（`Trie` 树） `s.pinyin`
> 6. 繁体转简体 `s.han`
> 7. 提取关键字 `s.keywords(limit=5)`
> 8. 信息衡量 `s.tf` 
>    - 词频越大越重要
> 9. 训练
>    - `from snownlp import seg`
>    - 结果更准确



**4c\3nlp\p2_sentiment.py**

> 1. 加载爬虫的原始评论数据 `pd.read_csv()`
> 2. 封装一个情感分析的函数
>    - 计算词性
>    - 计算评价：情感分析结果 `0.99560822 ...`
> 3. 查看结果 `df.head()`
>    - 默认前 `5` 个
> 4. 分析平均值 `df.sentiment.mean()`
>    - 根据星级进行拆分
> 5. 训练并导出 `df.to_csv()`



### 1.11.4. 本节总结

> 1. 二义：好 / 不好
> 2. 注意大小写 `snownlp -> SnowNLP`
> 3. 训练模型：高级算法





# 2. 本周作业

## 2.1. 作业说明

**作业背景：**在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

**作业要求：**请将以下的 SQL 语句翻译成 pandas 语句：

```sql
1. SELECT * FROM data;

2. SELECT * FROM data LIMIT 10;

3. SELECT id FROM data;  //id 是 data 表的特定一列

4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;

```



## 2.2. 作业解析

作业解答链接：https://github.com/maqiang626/Python004/tree/master/Week04/job



实现过程：

> 1. 初始化 data / table1 / table2 数据
> 2. 结合 numpy 和 pandas 进行数据处理



代码说明：

> 1. 使用 pandas DataFrame 初始化数据
> 2. 对比 sql 语句和 DataFrame 功能





# 3. 学习总结

## 3.1. 收获

1. 学习了 `numpy` 相关知识
2. 学习了 `pandas` 相关知识
3. 分词
4. 情感分析



## 3.2. 问题及不足

1. 涉及 `numpy` 和 `pandas` 的相关知识点众多
2. 应用场景



## 3.3. 改进

### 3.3.1. 深入学习

1. 更多的总结和学习 `numpy` 和 `pandas` 的相关知识
2. 多结合场景进行实际应用



### 3.3.2. 实践

1. 课程上所有代码全部手动过一遍
2. 作业先完成，后续再持续完善
3. 课下多写代码多思考，只有不断练习并学以致用，才能更快速提升自己



## 3.4. 感悟

1. 机器学习博大精深，让人望而却步
2. 对比 `Excel` 和 `pandas` 功能
3. `numpy` 和 `pandas`，难兄难弟
4. 后续使用网页 `Django` 展示分词和情感分析的结果

