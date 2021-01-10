#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:insert_Sort.py
@time:2021/01/10/21:11
"""
import random
from cal_time import  *
import copy

@cal_time()
def insert_Sort1(li):
    for i in range(1,len(li)):
        tmp=li[i]

        for j in range(i-1,-1,-1):
            if tmp>li[j]:
                li[j+1]=li[j]
                if j==0:##？？如何处理j=0的情况？？特殊处理
                    j-=1
                #print('exchange',j,li)
            else:
                #print('break', j, li)
                break
        li[j+1] = tmp
        #print(li)
    return  li

@cal_time()
def insert_Sort(li):
    for i in range(1,len(li)):
        tmp=li[i]
        j=i-1
        while j>=0 and tmp>li[j]:
                li[j+1]=li[j]
                j-=1
                #print('exchange',li)
        li[j+1] = tmp
        #print(li)
    return  li

if __name__ == '__main__':
    #ilist=[8,9,4,5,6]
    ilist = list(range(10000))
    random.shuffle(ilist)
    li1=copy.deepcopy(ilist)
    li2 = copy.deepcopy(ilist)
    #print(ilist)
    print('ready to do')
    insert_Sort1(li1)
    insert_Sort(li2)
