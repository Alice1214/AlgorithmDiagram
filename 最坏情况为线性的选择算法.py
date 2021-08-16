# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 最坏情况为线性的选择算法【此算法跟随机选择算法的区别是其主元不是随机选择的：首先将数组分为n/5组(这里5换成3不行，
#          7,9..可以)，除了最后一组可以不足五个元素，其余每组五个元素；寻找n/5组中每组的中位数（对每组元素进行插入排序，然
#          后确定有序元素的中位数）；对上一步中得到的中位数递归调用select,找到其中位数x,将x作为主元】；最坏情况为线性时间。
# Author:  HuiHui
# Date:    2019-02-27
# Reference: 网易公开课-算法导论P123
#################################

def local_sort(A,p,r):#对数组A的p to r部分进行插入排序
    for j in range(p+1,r+1):
        x=A[j]
        for i in range(j,p-1,-1):#找x的正确位置i；注意不能将x与A[i](i从j-1开始到p)比较,直到遇到A[i]<=x时认为i+1为x的正确
                                 #位置。因为若x的正确位置其实是p=i+1,我们需遇到A[i=p-1]<=x,但这超出了i的范围。
            if A[i-1]>x:
                A[i]=A[i-1]
            else:
                break
        A[i]=x
    return A

def median(A, p, r ):####分组并排序,记录每组中位数,并返回中位数对应到A中位置t（即主元位置）

    ####分组并排序,记录每组中位数
    long = r - p + 1  # A[p]到A[r]的长度
    if long // 5 == 0:
        return r
    B = []
    for i in range(1, long // 5 + 1):
        A = local_sort(A, p + 5 * (i - 1), p + 5 * i - 1)  # 逐段对每五个元素进行插入排序
        B.append(A[p + 5 * i - 3])  # 记录每组中位数
    B_0 = B
    mid = select(B_0, 0, len(B_0) - 1, len(B_0) // 2)  # 用select找出上述所有中位数的中位数

    ##????????给出中位数对应到数组B中的位置t_0和A中位置t（即主元位置）
    for i in range(0, len(B)):
        if B[i] == mid:
            t_0 = i
            t = p + 5 * (t_0 + 1) - 3
            break
    return t

def modified_partition(A,p,r):#随机划分，返回主元重排后的位置
    t=median(A, p, r )#主元
    A[t],A[r]=A[t],A[r]#主元放末尾
    x=A[r]
    m=p-1
    for j in range(p,r):
        if A[j]<=x:
            m=m+1
            A[m],A[j]=A[j],A[m]
    A[m+1],A[r]=A[r],A[m+1]
    return m+1

def select(A,p,r,i):
    if p==r:
        return A[p]
    q=modified_partition(A,p,r)
    k=q-p+1#
    if k==i:#递归基线条件
        return A[q]
    if k>i:
        return select(A,p,q-1,i)#在q之前得数组中查找
    if k<i:
        return select(A,q+1,r,i-k)#在q之后得数组中查找

def MININU(A):#找最小值的方法（i=1）
    min=A[0]
    for j in range(1,len(A)):
        if min>A[j]:
            min=A[j]
    return min

###############################
def main():
    Q= [89, 10, 21, 5, 2, 8, 33, 27, 63,55,66]
    B=MININU(Q)
    A=select(Q,0,10,11)
    print(A)
    print(B)

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()


########总结###########
#1.？处是否可以用其他方法
#2.主元一定要放末尾吗
