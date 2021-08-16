# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 基数排序（不同于比较排序，桶排序改进，稳定排序）；从末位开始；其时间复杂度为O(n+k)
# Author:  HuiHui
# Date:    2019-01-25
# Reference: 网易公开课-算法导论
#################################
def radix_sort(a):
    i=0#从个位开始排序
    n=1#最小位数为1
    max_number=max(a)#待排序中的最大数
    while max_number>= pow(10,n):#求最大数的位数
        n+=1
    while i<n:
        bucket={} #用字典构建桶
        for p in range(10):#将桶置空
            bucket.setdefault(p,[])
        for x in a:#将a中元素放到相应的基数桶中
            radix=int((x/pow(10,i))%10) #求得是x/pow(10,i)的个位数，i=0即为x的个位,i=1即为x的十位数，....
            bucket[radix].append(x)
        j=0
        for q in range(10):#取出桶中的数放回a中
            if len(bucket[q])!=0: #桶非空
                for y in bucket[q]: #将桶中元素放回a中
                    a[j]=y
                    j+=1
        i+=1
    return a

###############################
def main():
    A=[359,358,348]
    B=radix_sort(A)
    print(B)

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()

