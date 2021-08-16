# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: HASH表（处理冲突的方法：开放寻址法h(k,i)=(h'(k)+i)）mod m )；查找的时间为O(1)
# Author:  HuiHui
# Date:    2019-04-01
# Reference: 网易公开课-算法导论
#            https://www.cnblogs.com/dairuiquan/p/10509416.html
#################################
#创建与内建类型list相似的数组，其初始元素均为None
class Array(object):                        #新式类，解决了就是类多类继承的顺序问题。
    def __init__(self, size=32, init=None): #__**__是python魔法方法，具有特殊的调用方式;__**表私有属性和方法；_**有什么含义？
        self._size = size
        self._items = [init]*size
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index]=value
    def __len__(self):
        return self._size
    def clear(self,value=None):
        for i in range(self._size):
            self._items[i]=value
    def __iter__(self):  #使得Array是可迭代的，如可通过for实现循环
        for item in self._items:
            yield item   #生成器，函数中每次使用yield产生一个值，函数就返回该值，然后停止执行，等待被激活，被激活后继续在原来的位置执行

#定义哈希表数组的槽
#注意：一个槽有三种状态
#1. 从未被使用过，HashMap.UNUSED。 此槽没有被使用和冲突过，查找时只要找到UNUSED 就不用再继续探查了
#2. 使用过但是remove了，此时是HashMap.EMPTY，该谈差点后面的元素仍可能是有key
#3. 槽正在使用Slot节点
class Slot(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

#定义哈希表；采用开放寻址法解决冲突；线性探查
class HashTable(object):
    UNUSED=None            #表示slot从未被使用过
    EMPTY=Slot(None,None)  #表示slot被使用过但删除了
    def __init__(self,size):
        self._table=Array(size,init=self.UNUSED)
        self.length=0         #已装载的元素数量

    @property                 #内置装饰器，把方法变成属性
    def _load_factor(self):   #装载因子属性
        return self.length/float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self,key,i):                       #i从0到len(self._table)-1
        return abs(hash(key)+i)%len(self._table) #hash是内置函数,len(self._table)是槽数;线性探查

    def _rehash(self):  # 哈希表已满，重新哈希化
        old_table = self._table
        new_size = len(self._table) * 2
        self._table = Array(new_size, self.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not self.UNUSED and slot is not self.EMPTY:  #判断这个slot是有值的
                for i in range(new_size):
                    index = self._hash(slot.key, i)
                    if self._table[index] is self.UNUSED:           #将旧表中的槽插入新
                        self._table[index] = slot
                        self.length += 1
                        break

    def hash_search(self, key):        #返回key对应的index,value;若没找到，返回-1,None
        _len=len(self._table)
        for i in range(_len):          #线性探查，直至找到key,或者找到从未被使用的槽
            index = self._hash(key, i)
            if self._table[index] is self.UNUSED:
                print("Not Find %s" % key)
                return -1, None
            if self._table[index].key==key:
                print("Find %s index is %d,value is %d" % (key,index,self._table[index].value))
                return index,self._table[index].value
        print("Not Find %s"%key)       #探查完所有的槽都没找到key
        return -1,None

    def hash_insert(self, key, value):
        _len = len(self._table)
        for i in range(_len):  #线性探查，若找到表中已有key，则更新key的value；若找到从未被使用的槽或使用过但删除了的槽，则将key,value插入
            index = self._hash(key, i)
            if self._table[index] is self.EMPTY or self._table[index] is self.UNUSED:
                self._table[index]=Slot(key, value)          #注意这里若self._table[index]未被使用，即为None时,不能直接用.key,.value赋值
                print("Change %s value to %d" % (key, value))
                self.length+=1
                if self._load_factor>=0.8:
                    self._rehash()
                return 1
            if self._table[index].key==key:
                self._table[index].value = value
                print("Change %s value to %d" % (key,value))
                return 0         #返回0表示没有执行插入操作，执行的是更新操作
        print("Can Not Insert")  #探查完所有的槽都没找到能插入的地方
        return -1

    def hash_remove(self, key):
        index, value = self.hash_search(key)
        if index!=-1:                      #找到了key
            self._table[index]=self.EMPTY  #这里不能直接用.key=None,..
            self.length-=1
            print("Remove successful")
            return 1
        else:                              #没找到key
            print("Not Find %s" % key)
            return -1

    def __iter__(self):    #迭代器,遍历槽；
        for slot in self._table:
            if slot is not self.EMPTY and slot is not self.UNUSED:#slot有值
                yield slot #这里改为slot.key,则遍历的时key

###############################
def test_hash_table():
    h = HashTable(3)
    h.hash_insert('a', 0)
    h.hash_insert('b', 1)
    h.hash_insert('c', 2)
    print(len(h))
    h.hash_search('a')
    h.hash_search("d")
    h.hash_remove("a")
    for slot in h:
        print(slot.key,slot.value)
    print(h._load_factor)

###############################
def main():
    test_hash_table()

if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    main()

