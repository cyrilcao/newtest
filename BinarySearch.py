#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:BinarySearch.py
@time:2021/01/08/20:00
"""
from logit import  *
from cal_time import  *
import random

@logit()
def dolog():
    print('logging')

@cal_time()
def BinarySearch(iList1,val):
    left=0
    right=len(iList1)-1
    ##print('iList len is %s'%right)
    while left <= right:
        mid=(right+left)//2
        #print('mid value is %s'%iList1[mid])
        if val>iList1[mid] :
            left=mid+1
        elif val<iList1[mid] :
            right=mid-1
        else:
            print('find %s in list'%val)
            return mid
    print('Not found in list')
    return None

if __name__ == '__main__':
    ilist = list(range(100000))
    random.shuffle(ilist)
    print('ready to do')
    BinarySearch(ilist,77777)