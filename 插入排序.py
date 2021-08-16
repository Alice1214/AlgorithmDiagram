# !/usr/bin/env python
# -*- coding=utf-8 -*-
'''Summary: 插入排序（从小到大）--将第j个数插入到前j-1个数的合适位置，其时间复杂度为O(n^2)'''
# Author:  HuiHui
# Date:    2019-01-07
# Reference: 网易公开课-算法导论

def insert_sort(A):
    A_len=len(A)
    for i in range(1,A_len):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key
    for i in range(A_len):
        print(A[i])


def main():
    A=[4,2,6,9,3,1]
    insert_sort(A)

if __name__=='__main__': #当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()