#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:quick_sort.py
@time:2021/01/10/23:25
"""
import  random

def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and tmp<=li[right]:    #从右面找比tmp小的数的下标
            right-=1                #把右边界往左移一步
        li[left]=li[right]          #把右边的值写到左边
        while left<right and tmp>=li[left]:     #从左边找比tmp大的数的下标
            left+=1                 #把左边界右移一步
        li[right]=li[left]          #把左边的值写到右边
    li[left]=tmp            #tmp归位
    return left             #返回归为的位置标

def quick_sort(li,left,right):
    mid=partition(li,left,right)  #先找到归为的值
    quick_sort(li,left,mid-1)     #对mid左边的数递归归位
    quick_sort(li,mid+1,right)    #对mid右边的数递归归位

if __name__ == '__main__':
    ilist=[8,9,4,5,6,1,2,3,11]
    #ilist = list(range(100))
    random.shuffle(ilist)
    quick_sort(ilist,0,len(ilist)-1)