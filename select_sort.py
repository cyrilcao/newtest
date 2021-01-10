#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:select_sort.py
@time:2021/01/10/19:33
"""
import random
def select_simple_sort(li):
    newli=[]
    for i in range(0,len(li)):
        print('------------%s'%i)
        min_val=min(li)
        newli.append(min_val)
        li.remove(min_val)
        print(i,li)
        print(i,newli)
    return newli

def select_sort(li):
    for i in range(len(li)):
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                li[j],li[min_loc]=li[min_loc],li[j]
    return li

if __name__ == '__main__':
    ilist = list(range(10))
    random.shuffle(ilist)
    print(ilist)
    print('ready to do')
    print( select_sort(ilist))