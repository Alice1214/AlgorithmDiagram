# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 归并排序（从小到大，分治算法）--将数列分成有序子序列，再将有序子序列归并成一个有序列；拆分-排序-合并；其时间复杂度为O(n*log n)'''
# Author:  HuiHui
# Date:    2019-01-07ed2k://|file|SW_DVD5_Office_Professional_Plus_2010_64Bit_ChnSimp_MLF_X16-52534.iso|1009090560|C0BADE6BE073CC00609E6CA16D0C62AC|/
# Reference: 网易公开课-算法导论

#排序、归并
def merge(l_list,r_list):
    result=[]#存储归并列
    while len(l_list)>0 and len(r_list)>0:
        if l_list[0]<=r_list[0]:#排序
            result.append(l_list.pop(0))
        else:
            result.append(r_list.pop(0))
    if len(l_list)>0:#如果某一列已经归并完，另一列还有剩余元素，则将剩余元素全部添加到归并列的末尾
        result.extend(l_list)
    if len(r_list)>0:
        result.extend(r_list)
    return result


def merge_sort(A):
    A_len=len(A)
    if A_len==1:
        return A
    #拆分
    mid=A_len//2
    left=A[:mid]
    right=A[mid:]
    l_list=merge_sort(left)
    r_list=merge_sort(right)
    #排序、归并
    merge_list=merge(l_list,r_list)
    return merge_list
###############################
def main():
    A=[4,2,4,9,3]
    B=merge_sort(A)
    print(B)

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()