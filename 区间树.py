# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 区间树（假设都是闭的）
# Author:  HuiHui
# Date:    2019-07-09
# Reference:
#################################
import queue

class interval(object): #-----------定义区间类
    def __init__(self,low,high):
        self.low = low
        self.high = high

class ITNode(object):#定义区间树节点类（多了int,max属性:max表示以self为根节点的子树中所有区间端点最大值）
    def __init__(self,low,high,color="R"):
        self.int=interval(low,high)
        self.max=high   #附加信息

        self.val = self.int.low
        self.color = color
        self.left,self.right,self.father = None,None,None
    def is_black_node(self):
        return self.color=="R"
    def set_black_node(self):
        self.color = "B"
    def set_red_node(self):
        self.color = "R"
    def print(self):#按先序遍历顺序打印以TreeNode为根节点的子树的所有区间
        if self.left:
            self.left.print()
        print(self.int.low,self.int.high)
        if self.right:
            self.right.print()

class IT(object):#扩展红黑树构建区间树（修改插入、删除操作；添加interval_search()新操作）
    def __init__(self,nodeList):
        self.nil=ITNode(-1,-1,color="B")
        self.root = self.nil
        for node in nodeList:
            self.IT_insert(node)

    def interval_search(self,i):#-------------查找区间树中与区间i重叠的结点，若不存在则返回nil;O(lgn)
        x=self.root
        while x!=self.nil:
            if x.int.low<=i.high and i.low<=x.int.high:
                return x
            elif i.high<x.int.low:
                x=x.left
            else:
                x=x.right
        return x

    def left_rotate(self, node):      #左旋(三步)  《要求node.right!=None,否则不能左旋》《注意空节点》
        p=node.father
        right=node.right
        #（1）
        node.right=right.left
        if right.left!=self.nil:
            right.left.father=node
        #（2）
        right.left=node
        node.father=right
        #（3）
        right.father = p
        if p==self.nil:#表明node是根节点
            self.root=right
        elif p.left==node:
            p.left=right
        else:
            p.right = right
        # ------------------维护max属性
        right.max = node.max
        node.max = max(node.int.high, node.left.max, node.right.max)
        return 1
    def right_rotate(self, node):      #右旋(三步)  《要求node.left!=None,否则不能右旋》《注意空节点》
        p=node.father
        left=node.left
        #（1）
        node.left=left.right
        if left.right!=self.nil:
            left.right.father=node
        #（2）
        left.right=node
        node.father=left
        #（3）
        left.father = p
        if p==self.nil:#表明node是根节点
            self.root=left
        elif p.left==node:
            p.left=left
        else:
            p.right=left
        #------------------维护max属性
        left.max=node.max
        node.max=max(node.int.high,node.left.max,node.right.max)
        return 1

    # 插入：从根节点开始遍历树，找node父节点的位置《红黑树的插入需调用RBT_insert_fixup（）重新着色并旋转以保证红黑树性质》
    def IT_insert(self,node):
        cur=self.root#存放当前遍历到的节点
        father = self.nil#存放node的父节点
        while cur!=self.nil:           #找到一个空的位置来插入node
            father = cur
            if node.val<cur.val:   #插入左子树
                cur=cur.left
            elif node.val>cur.val: #插入右子树
                cur=cur.right
            else:                  #值相等，则插入失败
                print("%d is already in Tree" % node.val)
                return -1
        node.father = father  # node的父节点
        if node.father==self.nil: #表明树是空的
            self.root=node
        elif node.val<father.val:
            father.left=node
        else:
            father.right=node
        node.left=self.nil    #左右孩子指向黑色哨兵节点，以便于处理边界条件
        node.right=self.nil
        node.color="R"

        node.max = max(node.int.high, node.left.max, node.right.max) #----------维护node的max属性
        self.IT_insert_fixup(node)   #重新着色并旋转以保证红黑树性质
        #print("%d insert successfully" % node.val)

        #---------------更新node所有祖先的max
        while node.father!=self.nil:
            node.father.max=max(node.father.max,node.max)
            node=node.father
        return 1
    def IT_insert_fixup(self,node):   #重新着色并旋转以保证红黑树性质：按node父节点是爷爷节点的左右孩子分成两类，每一类分别有三种情况
        while node.father.color=="R":         #当node父节点为黑色时结束循环
            if node.father==node.father.father.left:       #   1.父节点是左孩子
                uncle=node.father.father.right #叔节点
                if uncle.color=="R":                       #    （1）红父，红叔： 将父叔变成黑色；将爷节点变成红色；将爷节点赋值给node
                    node.father.color="B"
                    uncle.color="B"
                    node.father.father.color="R"
                    node=node.father.father
                else:
                    if node==node.father.right:            #     (2)红父、黑叔、node是右孩子：左旋node.father,变成情况（3）
                        node=node.father
                        self.left_rotate(node)
                    node.father.color="B"                  #     (3)红父、黑叔、node是左孩子：父节点爷节点变色，右旋爷节点
                    node.father.father.color="R"
                    self.right_rotate(node.father.father)
            else:
                uncle = node.father.father.left
                if uncle.color == "R":
                    node.father.color = "B"
                    uncle.color = "B"
                    node.father.father.color = "R"
                    node = node.father.father
                else:
                    if node == node.father.left:
                        node = node.father
                        self.right_rotate(node)
                    node.father.color = "B"
                    node.father.father.color= "R"
                    self.left_rotate(node.father.father)
        self.root.color="B"          #当node为根节点时，颜色修正为黑色即可
        return 1

    ##删除：
    def Tree_Minimum(self,node):#返回树的最小值
        while node.left!=self.nil:
            node=node.left
        return node
    def IT_transplant(self,u,v): #用以v为根节点的子树替换以u为节点的子树
        if u.father==self.nil:
            self.root=v
        elif u==u.father.left:
            u.father.left=v
        else:
            u.father.right=v
        v.father=u.father  #这里即使v指向哨兵，也能给其父节点赋值，因此无条件语句
    def IT_delete_fixup(self,x):#修正删除破坏的红黑树性质（主要解决黑高被破坏的问题，即x.color=="B"）
        while x!=self.root and x.color=="B":
            if x==x.father.left:
                w=x.father.right #x是双重黑色结点，故w不可能是nil
                if w.color=="R":   #   (1)红兄：此时其父节点和孩子节点都是黑色：改变某些结点颜色并左旋父节点（不改变红黑树性质），则变成情况（2）或（3）（4）
                    x.father.color="R"
                    w.color="B"
                    self.left_rotate(x.father)
                    w=x.father.right
                if w.left.color=="B" and w.right.color=="B": #   (2)黑兄，且其孩子节点均为黑：将w变为红色，新的x指向x.father,循环结束会为其着黑色
                    w.color="R"
                    x=x.father
                elif w.right.color=="B": #(3)黑兄，左孩子红，右孩子黑：w.left变成黑色，w变成红色，右旋w,重新赋值w,变成情况（4）
                    w.left.color="B"
                    w.color="R"
                    self.right_rotate(w)
                    w=x.father.right
                w.color=x.father.color     #（4）黑兄，右孩子红：交换x.father与w的颜色，w.right着黑色，左旋x.father
                x.father.color="B"
                w.right.color="B"
                self.left_rotate(x.father)
                x=self.root
            else:
                w = x.father.left
                if w.color == "R":
                    x.father.color = "R"
                    w.color = "B"
                    self.right_rotate(x.father)
                    w = x.father.left
                if w.left.color == "B" and w.right.color == "B":
                    w.color = "R"
                    x = x.father
                elif w.left.color == "B":
                    w.right.color = "B"
                    w.color = "R"
                    self.left_rotate(w)
                    w = x.father.left
                w.color = x.father.color
                x.father.color = "B"
                w.left.color = "B"
                self.right_rotate(x.father)
                x = self.root
        x.color="B"
        return 1
    def IT_delete(self, node):  ##删除节点：
        y=node #记录要删除的结点
        y_original_color=y.color #记录要删除结点的原始颜色，用于最后检查是否破坏红黑树性质
        if node.left ==self.nil: #   1.左子树空
            x=node.right #记录用来替换被删除结点的结点，如果经判断，需要修正删除结点后的红黑树的性质，则从该结点处开始修正
            self.IT_transplant(node,node.right)
        elif node.right==self.nil: #   2.右子树空
            x=node.left
            self.IT_transplant(node, node.left)
        else:     #       3.左右子树均不空：将node于其后继交换位置，并将node的颜色赋给后继，再删除后继位置上的node即可
            y=self.Tree_Minimum(node.right) #node的后继
            y_original_color=y.color
            x=y.right
            if y.father==node: #(1) 这种情况不能直接调用transplant,会使得x.father指向node,导致RBT_delete_fixup(x)出错
                x.father=y # 注意y.right为nil时，其父节点也需指向y，否则RBT_delete_fixup(x)会出错
            else:              #(2)
                self.IT_transplant(y,y.right)
                y.right=node.right
                y.right.father=y
            self.IT_transplant(node,y)
            y.left=node.left
            y.left.father=y
            y.color = node.color
        #----------维护要删除的结点的父节点至根节点的max属性
        g=y.father
        while g.max==y.max and g!=self.nil:
            g.max = max(g.int.high, g.left.max, g.right.max)
            g = g.father

        if y_original_color=="B":
            self.IT_delete_fixup(x)
        return 1

    def IT_to_ValColorMaxList(self):#生成二叉搜索树值的列表及颜色列表:利用队列先进先出的特性，按从上往下，从左往右的顺序排序
            if self.root==self.nil:
                print("tree is empty!")
                return -1
            ValList=[]
            ColorList=[]
            MaxList=[]
            q=queue.Queue()
            q.put(self.root)
            while q.empty() is not True: #每次从队列取出一个值放入列表，并将其左右子节点放入队列中；直到队列为空，则树的值已全部放如列表中
                node=q.get()
                ValList.append(node.val)
                ColorList.append(node.color)
                MaxList.append(node.max)
                if node.left!=self.nil:   #插入左子树
                    q.put(node.left)
                if node.right!=self.nil: #插入右子树
                    q.put(node.right)
            return ValList,ColorList,MaxList

    '''def search(self,val):#查询：从根节点开始搜索树，直到遇到叶子节点
            if self.root==self.nil:
                print("tree is empty!")
                return 0
            cur=self.root   #存放当前遍历到的节点
            while cur!=self.nil:
                if val==cur.val:  #找到了val
                    print("%d is found" % val)
                    return cur
                elif val>cur.val:
                    cur=cur.right
                else:
                    cur=cur.left
            print("%d is not in tree" % val)
            return -1'''

####################################
if __name__ == '__main__':
    node2 = ITNode(2,3)
    node5 = ITNode(5,6)
    node8 = ITNode(8,9)
    node=ITNode(0,4)

    i1=interval(0,1)
    i2=interval(9,9)
    tree=IT([node5,node2,node8])

    a,b,c=tree.IT_to_ValColorMaxList()
    print(a,b,c)
    print("next")

    print(tree.interval_search(i1).val)
    print(tree.interval_search(i2).val)
    print("next")

    tree.IT_insert(node)
    a, b, c = tree.IT_to_ValColorMaxList()
    print(a, b, c)
    print("next")

    tree.IT_delete(node)
    a, b, c = tree.IT_to_ValColorMaxList()
    print(a, b, c)
    print("next")

