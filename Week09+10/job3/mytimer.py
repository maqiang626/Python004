#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04C19301 maqiang <maqiang626@qq.com> [2020-12-06 22:00 +0800]
# Verified: Windows 10 20H2 &&& Python v3.7.9
#
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数
#
# ==================================================================
#


from functools import wraps
import time
import random


def timer(func):
    """装饰器

    1. 记录函数的运行时间
    2. 被装饰函数带不定长参数
    """

    @wraps(func)
    def calctime(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'<{func.__name__}> running time: {end_time - start_time} (s)')
    return calctime


@timer
def myfunc(a, b):
    """随机暂停时间"""
    time.sleep(random.uniform(a, b))


if __name__ == '__main__':
    myfunc(2, 6)
