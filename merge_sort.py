#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:merge_sort.py
@time:2021/01/13/14:57
#归并排序

[low，，，，，，mid,mid+1,,,,,high]
[i，，，，，，mid,j,,,,,high]
两两对比，对比后大的数放置新队列，i++ or j++
"""
import sys
sys.setrecursionlimit(10000)


###对两个有序队列归并成一个有序队列
def listmerge(li,low,high):
    mid=(low+high)//2  #取中间数
    i=low
    j=mid+1
    litmp=[]
    while i<=mid and j<=high :
        #print(i,mid,j)
        if li[i]<li[j]:
            litmp.append(li[j])
            j+=1
            continue
        if li[j]<=li[i]:
            litmp.append(li[i])
            i+=1
            continue
    while i<=mid:
        litmp.append(li[i])
        i+=1
    while j<=high :
        litmp.append(li[j])
        j+=1
    li[low:high+1]=litmp

def merge_sort(li,low,high):
    if low<high:  #当至少有2个元素时
        #print(low,high)
        mid=(low+high)//2  #找中间值
        merge_sort(li,low,mid)  #对前面一半队列排序
        merge_sort(li,mid+1,high) #对后面一半队列排序
        listmerge(li,low,high)   #两个有序队列归并成一个有序队列


if __name__ == '__main__':
    li=[3,2,1,0,5,4]
    merge_sort(li,0,5)
    print(li)
    #print(1//2)
    pass