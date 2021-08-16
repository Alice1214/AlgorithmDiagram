# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 动态规划-最长公共子序列(1.最优子结构：一个问题的最优解包含其子问题的最优解；2.重叠子问题：问题的递归算法会反复求解相同的子问题)
# Author:  HuiHui
# Date:    2019-07-10
# Reference:
#################################

def LCS_length(x,y):#返回序列A与B的最长公共子序列的长度
    len1=len(x)
    len2=len(y)
    c=[[0 for j in range(len2+1)] for i in range(len1+1)] #c[i,j]记录A[0:i]和B[0:j]的最长公共子序列的长度
    b=[[0 for j in range(len2+1)] for i in range(len1+1)] #b[i,j]指向对应计算c[i,j]时所选择的子问题最优解（注：从b[1,1]开始）
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]="、"
            elif c[i][j-1]>=c[i-1][j]:
                c[i][j] = c[i][j - 1]
                b[i][j] = "-"
            else:
                c[i][j] = c[i-1][j]
                b[i][j] = "|"
        print(c[i][1:])
        print(b[i][1:])
    return c[len1][len2],b
def LCS_print(b,x,i,j):#打印最长公共子序列
    if i==0 and j==0:
        return
    elif b[i][j]=="、":
        LCS_print(b, x, i-1, j-1)
        print(x[i-1])
    elif b[i][j] == "-":
        LCS_print(b, x, i, j - 1)
    else:
        LCS_print(b, x, i-1, j)


####################################
if __name__ == '__main__':
    x=["A","B","B","A","A"]
    y=["B","A","A","B"]
    a,b=LCS_length(x,y)
    print(a)
    LCS_print(b,x,5,4)
