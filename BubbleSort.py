#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:BubbleSort.py
@time:2021/01/10/20:02
"""
import random
def Bubble_Sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange =True
        print(i,li)
        if not exchange:
            print('未交换，退出')
            return  li
    return li

if __name__ == '__main__':
    ilist = list(range(10))
    random.shuffle(ilist)
    print(ilist)
    print('ready to do')
    print(Bubble_Sort(ilist))