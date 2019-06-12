#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/12/2019 14:34
# @Author   : mingfei.net@gmail.com
# @FileName : generator.py
# @GitHub   : https://github.com/thu/project-0610

list_a = list(range(1, 11))

print(list_a)

list_a = [x**2 for x in range(1, 11)]

g_a = (x**2 for x in range(1, 5))

print(list_a)
print(type(g_a))

print(next(g_a))
print(next(g_a))
print(next(g_a))
print(next(g_a))
# print(next(g_a))

for n in g_a:
    print(n)