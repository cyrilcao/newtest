# -*- coding: utf-8 -*-  
#  Author:cyril  Date:
# @time:2021/01/08/18:32
# 汉诺塔问题计算


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('move from---%s--to---%s' % (a, c))
        hanoi(n - 1, b, a, c)


if __name__ == '__main__':
    print('test')
    hanoi(5, 'a', 'b', 'c')
    pass

