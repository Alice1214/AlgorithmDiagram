# !/usr/bin/env python
# -*- coding=utf-8 -*-
#Summary: 进程和线程学习
# Author: HuiHui
# Date:   2018-11-27
# Reference: https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868323401155ceb3db1e2044f80b974b469eb06cb43000
import os
from multiprocessing import Pool
from multiprocessing import Process
import threading
import random,time

def f1(i,n):
    time.sleep(1)
    print("%d-->%s--->%s"%(i,os.getpid(),time.ctime()))
    return n*n


if __name__=="__main__":
    print("%s start..."%os.getpid())
    p=Pool(4)
    res_l=[]
    for i in range(10):
        res=p.apply(func=f1,args=(i,i))
        res_l.append(res)


    '''p.close()
    p.join()
    
    for res in res_l:
        print(res.get())'''
    print(res_l)
    print("%s end..."%os.getpid())
    print(os.cpu_count())


