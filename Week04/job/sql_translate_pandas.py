#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04BB8801 maqiang <maqiang626@qq.com> [2020-10-25 19:50 +0800]
# Verified: Windows 10 1803 &&& Python v3.7.9
#
# 请将以下的 SQL 语句翻译成 pandas 语句 (共 10 条 SQL 语句)
#
# ==================================================================
#


import numpy as np
import pandas as pd


# 初始化 data 数据
data_size = 2020
data = pd.DataFrame({
    "id": np.random.randint(1, 10000, data_size),
    "age": np.random.randint(18, 80, data_size)
})

# 初始化 table1 数据
table1_size = 100
table1 = pd.DataFrame({
    "id": np.random.randint(1, 200, table1_size),
    "order_id": np.random.randint(1000, 6000, table1_size)
})

# 初始化 table2 数据
table2_size = 200
table2 = pd.DataFrame({
    "id": np.random.randint(1, 500, table2_size),
    "age": np.random.randint(20, 60, table2_size)
})

# SQL 1. SELECT * FROM data;
print('=================== SQL 1. SELECT * FROM data; ===================')
print(data)
print('\n')

# SQL 2. SELECT * FROM data LIMIT 10;  (两种方法)
print('============== SQL 2. SELECT * FROM data LIMIT 10;  ==============')
print(data.head(10))
print('\n')
print(data.loc[0:9])
print('\n')

# SQL 3. SELECT id FROM data;  (两种方法)
print('================== SQL 3. SELECT id FROM data;  ==================')
print(data['id'])
print('\n')
print(data.iloc[:, [0]])
print('\n')

# SQL 4. SELECT COUNT(id) FROM data;
print('=============== SQL 4. SELECT COUNT(id) FROM data; ===============')
print(data['id'].size)
print('\n')

# SQL 5. SELECT * FROM data WHERE id<1000 AND age>30;
print('====== SQL 5. SELECT * FROM data WHERE id<1000 AND age>30;  ======')
print(data[(data['id'] < 1000) & (data['age'] > 30)])
print('\n')

# SQL 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print('SQL 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;')
print(table1.groupby('id').agg({'order_id': pd.Series.nunique}))
print('\n')

# SQL 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print('SQL 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;')
print(pd.merge(table1, table2, on='id'))
print('\n')

# SQL 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print('==== SQL 8. SELECT * FROM table1 UNION SELECT * FROM table2;  ====')
print(pd.concat([table1, table2]).drop_duplicates())
print('\n')

# SQL 9. DELETE FROM table1 WHERE id=10;
print('============= SQL 9. DELETE FROM table1 WHERE id=10; =============')
print(table1.drop(table1.query('id==10').index, axis=0))
print('\n')

# SQL 10. ALTER TABLE table1 DROP COLUMN column_name;
print('====== SQL 10. ALTER TABLE table1 DROP COLUMN column_name;  ======')
print(table1.drop('id', axis=1))
