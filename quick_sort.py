#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:quick_sort.py
@time:2021/01/10/23:25
复杂度 O(nlogn)
"""
import  random
import sys
from cal_time import *
sys.setrecursionlimit(10000)  #修改递归深度

def partition(li,left,right):
    ##优化， 找一个随机数与第一个数互换
    rnd=random.randint(left,right)
    li[left],li[rnd]=li[rnd],li[left]
    ###
    tmp=li[left]
    while left<right:
        while left<right and tmp<=li[right]:    #从右面找比tmp小的数的下标
            right-=1                #把右边界往左移一步
        li[left]=li[right]          #把右边的值写到左边
        while left<right and tmp>=li[left]:     #从左边找比tmp大的数的下标
            left+=1                 #把左边界右移一步
        li[right]=li[left]          #把左边的值写到右边
    li[left]=tmp            #tmp归位
    #print(li)
    return left             #返回归为的位置标

def _quick_sort(li,left,right):
    if left<right :
        mid=partition(li,left,right)  #先找到归为的值
        _quick_sort(li,left,mid-1)     #对mid左边的数递归归位
        _quick_sort(li,mid+1,right)    #对mid右边的数递归归位

@cal_time()
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)

if __name__ == '__main__':

    #ilist=[9,8,7,6,5,4,3,2,1]  ##最坏情况
    ilist = list(range(10000,0,-1))
    #random.shuffle(ilist)
    quick_sort(ilist)
    #print(ilist)