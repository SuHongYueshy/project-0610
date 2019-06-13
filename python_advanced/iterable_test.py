#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/13/2019 09:50
# @Author   : mingfei.net@gmail.com
# @FileName : iterable_test.py
# @GitHub   : https://github.com/thu/project-0610


class Test(object):

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            t = self.i
            self.i = self.i + 1
            return t
        else:
            raise StopIteration('StopIteration...')


o = Test(10)


for i in o:
    print(i)
