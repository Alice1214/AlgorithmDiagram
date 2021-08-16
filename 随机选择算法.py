# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 随机选择（查找数组A的第i个顺序统计量，如i=1,则为最小值此时使用MININU()即可）；随机分治算法（从数组中随机取一
#          元素，将其作为主元对数组进行部分快速排序(即快排中的划分：将末尾的值与随机选取的主元交换位置，从p遍历到r-1,若
#          比主元小，则放到数列左边，最后将A[r]与左边最后一个比其小的位置的下一位置交换)，若排序后该元素的位置r刚好为k,
#          则第k小的数即为该元素，否则利用分治法的思想，比较r和k，若r比k小，则r之后的数组中利用相同的方法继续找数组A的
#          第i小的数，否则，在r之前的数组中查找）；其期望时间复杂度为O(n)
# Author:  HuiHui
# Date:    2019-02-23
# Reference: 网易公开课-算法导论
#################################
import random

def randomied_partition(A,p,r):#随机划分，返回主元重排后的位置
    t = random.randint(p, r)
    A[t],A[r]=A[r],A[t] #随机选取主元，并将其放到末尾
    x=A[r]
    m=p-1
    for j in range(p,r):
        if A[j]<=x:
            m=m+1
            A[m],A[j]=A[j],A[m]
    A[m+1],A[r]=A[r],A[m+1]
    return m+1

def randomied_select(A,p,r,i):
    if p==r:
        return A[p]
    q=randomied_partition(A,p,r)
    k=q-p+1#
    if k==i:#递归基线条件
        return A[q]
    if k>i:
        return randomied_select(A,p,q-1,i)#在q之前得数组中查找
    if k<i:
        return randomied_select(A, q+1, r, i-k)#在q之后得数组中查找

def MININU(A):#找最小值的方法（i=1）
    min=A[0]
    for j in range(1,len(A)):
        if min>A[j]:
            min=A[j]
    return min

###############################
def main():
    A = [89, 100, 21, 5, 2, 8, 33, 27, 63]
    B=MININU(A)
    C=randomied_select(A,0,8,2)
    print(B)
    print(C)

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()

