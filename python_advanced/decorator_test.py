#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/14/2019 10:26
# @Author   : mingfei.net@gmail.com
# @FileName : decorator_test.py
# @GitHub   : https://github.com/thu/project-0610


def a_decorator(func):

    def wrapper():
        print(func.__name__, 'before...')
        func()
        print(func.__name__, 'after...')

    return wrapper


def f():
    print('function f...')


# f()

a_decorator(f)()