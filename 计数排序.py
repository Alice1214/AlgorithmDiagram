# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 计数排序（不同于比较排序）；计数—记录位置-排序；其时间复杂度为O(n+k)
# Author:  HuiHui
# Date:    2019-01-24
# Reference: 网易公开课-算法导论
#################################
def counting_sort(list,k):
    n=len(list)
    result=[0 for i in range(n)]
    A=[0 for i in range(k+1)]#长度为k
    for i in range(n):#计数
        A[list[i]]+=1
    for i in range(1,k+1):#记录位置
        A[i]=A[i-1]+A[i]
    for i in range(n-1,-1,-1):#倒着遍历list,将元素放入result中正确的排序位置
        result[A[list[i]]-1]=list[i]
        A[list[i]]-=1
    return result

###############################
def main():
    A=[4,2,4,9,3]
    B=counting_sort(A,10)
    print(B)

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()

