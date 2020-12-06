#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04C09201 maqiang <maqiang626@qq.com> [2020-12-06 22:00 +0800]
# Verified: Windows 10 20H2 &&& Python v3.7.9
#
# 自定义一个 python 函数，实现 map() 函数的功能
#
# ==================================================================
#


def myfunc(x):
    """square"""
    return x**2


def mymap(func, iter):
    """模拟 map() 函数的功能

    1. func 函数对象，对可迭代对象中每个值进行处理
    2. iter 可迭代对象
    """

    if hasattr(iter, '__iter__'):
        for i in iter:
            yield func(i)
    else:
        raise TypeError(f'<{iter}> can not iterable')


if __name__ == '__main__':
    square = mymap(myfunc, range(10))
    next(square)
    list(square)
