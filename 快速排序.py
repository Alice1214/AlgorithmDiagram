# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 快速排序(列表从小到大有序，分治法)；其时间复杂度为O( )
# Author:  HuiHui
# Date:    2019-01-16
# Reference: 算法图解

def quick_sort(list):
    if len(list)<=1:#基线条件
        return list
    else:#缩小问题规模，使其符合基线条件（分）
        pivot=list[0]#基准值
        left=[]
        right = []
        for i in range(1,len(list)):
            if list[i]>=pivot:
                right.append(list[i])
            else:
                left.append(list[i])
        return quick_sort(left)+[pivot]+quick_sort(right)#排序，合

def main():
    A=[2,5,11,11,14,18]
    print(quick_sort(A))

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()