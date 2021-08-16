# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 二分法查找(列表从小到大有序)；其时间复杂度为O(log n)
# Author:  HuiHui
# Date:    2019-01-11
# Reference: 算法图解

def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:#只要还有范围没查到（包括仅有一个元素），就继续查找
        mid = (low + high) // 2
        guess=list[mid] #查找中间元素
        if guess==item:
            return mid
        if guess<item:
            low=mid+1
        if guess>item:
            high=mid-1
    return None

def main():
    A=[2,5,7,11,14,18]
    print(binary_search(A,11))
    print(binary_search(A,9))


if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()