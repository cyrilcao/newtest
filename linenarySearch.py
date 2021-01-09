#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:linenarySearch.py
@time:2021/01/09/22:21
"""
from cal_time import  *
import random

@cal_time()
def linenarySearch(iList,val):
    for i,element in enumerate(iList):
        if element==val:
            print('find %s in list' % element)
            return element
    else:
        print('not found')
        return None

if __name__ == '__main__':
    ilist = list(range(1000000))
    random.shuffle(ilist)
    print('ready to do')
    linenarySearch(ilist, 77777)