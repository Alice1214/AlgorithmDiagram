# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 贪心算法(1.最优子结构：一个问题的最优解包含其子问题的最优解；2.贪心选择性质：可通过局部最优解选择来构造全局最优解)(递归、迭代贪心算法：时间O(n))
# Author:  HuiHui
# Date:    2019-07-15
# Reference:
#################################
#递归贪心算法：返回最优活动组合的下标
def recursive_activity_selector(s,f,k,n):#s,f数组分别存储了活动的开始和结束时间，n表示活动个数，下标k表示求解子问题Sk;假设n个活动已按结束时间排好序。
    m=k+1
    while m<=n and s[m]<f[k]:
        m=m+1
    if m<=n:
        a=recursive_activity_selector(s,f,m,n)
        a.append(m)
        return a
    else:
        return []

#迭代贪心算法：
def greedy_activity_selector(s,f):#假设n个活动已按结束时间排好序。
    n=len(s)-1
    a=[1]
    k=1
    for m in range(2,n+1):
        if s[m]>=f[k]:
            a.append(m)
            k=m
    return a

####################################
if __name__ == '__main__':
    s=[0,1,2,3,4]#添加一个虚拟活动（0，0）
    f=[0,3,4,4,5]

    print(recursive_activity_selector(s,f,0,4))
    print(greedy_activity_selector(s, f))

