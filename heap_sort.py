#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:heap_sort.py
@time:2021/01/13/1:04
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

The strange invariant above is meant to be an efficient memory
representation for a tournament.  The numbers below are `k', not a[k]:

                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30


In the tree above, each cell `k' is topping `2*k+1' and `2*k+2'.  In


"""


##
import random


def sift(li,low,high):   ##把大的数向上调整
    tmp=li[low]  #存储堆顶元素
    i=low   #i指向根节点
    j = 2 * i + 1  #左孩子下标
    while j <=high:   #左孩子不超过界限
        if j+1<=high and li[j+1]>li[j]:#如果右孩子有且不超过界限
            j+=1  #指向右孩子
        if li[j]>tmp:  #如果孩子大于根节点
            li[i]=li[j] #孩子向上调整
            i = j       #根节点指向原来的孩子节点
            j = 2 * i + 1   #找下一层的左孩子
        else:
            li[i] = tmp     #tmp更大，把tmp放回领导位
            break
    else:
        li[i]=tmp           #把tmp放回原位


def heap_sort(li):
    ##建堆
    n=len(li)
    for i in range (n-2//2,-1,-1):
        sift(li,i,n-1)

    ##每次都把堆顶元素拿出来，再把最后一个元素放到顶，做向下调整

    for i  in range(n-1,-1,-1):
    #i指向堆最后一个元素
        li[i],li[0]=li[0],li[i]
        sift(li,0,i-1)      #i-1是新high

def sift_des(li,low,high):  ##把小的数向上调整
    tmp=li[low]  #存储堆顶元素
    i=low   #i指向根节点
    j = 2 * i + 1  #左孩子下标
    while j <=high:   #左孩子不超过界限
        if j+1<=high and li[j+1]<li[j]:#如果右孩子有且不超过界限
            j+=1  #指向右孩子
        if li[j]<tmp:  #如果孩子小于根节点
            li[i]=li[j] #孩子向上调整
            i = j       #根节点指向原来的孩子节点
            j = 2 * i + 1   #找下一层的左孩子
        else:
            li[i] = tmp     #tmp更大，把tmp放回领导位
            break
    else:
        li[i]=tmp           #把tmp放回原位

def heapk(li,k):
    if k<=len(li):
        topk=li[0:k]
        ##对前K个数建小根堆
        k = len(topk)
        for i in range(k - 2 // 2, -1, -1):
            sift_des(topk, i, k - 1)
        ##剩余数放堆顶做
        for i in range(k,len(li)):
            if li[i]>topk[0]:
                topk[0]=li[i]
                sift_des(topk,0,k-1)
        ##出数,排序
        for i in range(k-1,-1,-1):
            topk[0],topk[i]=topk[i],topk[0]
            sift_des(topk,0,i-1)
    return topk

import heapq

##系统自带heap方法
if __name__ == '__main__':
    li = list(range(10))
    random.shuffle(li)
    #heap_sort(li)
    print(heapk(li,4))

    pass