#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/12/2019 08:42
# @Author   : mingfei.net@gmail.com
# @FileName : day03.py
# @GitHub   : https://github.com/thu/project-0610

import os

list_a = [1, 2, 3]

print(list_a)

list_a = list(range(1, 11))

print(list_a)

list_a = []

for x in range(1, 11):
    list_a.append(x * x)

print(list_a)

list_b = [x * x for x in range(1, 11)]

print(list_b)

list_c = [f for f in os.listdir('.')]

print(list_c)

list_c = [f for f in os.listdir('.') if os.path.isfile(f)]

print(list_c)

list_a = [x for x in range(1, 11) if x % 2 == 0]

print(list_a)

list_d = [m + n + i for m in 'ABC' for n in 'XYZ' for i in '123']

# for m in 'ABC':
#     for n in 'XYZ':
#         list_d.append(m + n)

print(list_d)

d = {'a':'X', 'b':'Y', 'c':'Z'}

list_e = [k + '=' + v for k, v in d.items()]

print(list_e)

list_f = ['Hello', 'World']

list_f = [x.lower() for x in list_f]

print(list_f)


