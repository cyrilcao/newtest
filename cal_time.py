#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cyril
@file:cal_time.py
@time:2021/01/09/23:51
计时装饰器类
@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性
"""
import time
from functools import wraps

class cal_time(object):
    def __init__(self):
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            print('starting  cal_time')
            refunc=func(*args, **kwargs)
            print('eclapsed time :',  time.process_time())
            return refunc
        return wrapped_function
