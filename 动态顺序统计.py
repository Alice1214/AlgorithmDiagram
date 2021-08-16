# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 动态排序统计（由红黑树扩张的数据结构）
# Author:  HuiHui
# Date:    2019-06-27
# Reference:
#################################
import queue

class RBTNode(object):#添加了size属性，来记录x结点的子树结点数（包含x本身）
    def __init__(self, val,color="R"):
        self.val = val
        self.color = color
        self.size=0 #不能设为1，因为会导致计算size时，将self.nil的size当作1加进去
        self.left,self.right,self.father = None,None,None
    def is_black_node(self):
        return self.color=="R"
    def set_black_node(self):
        self.color = "B"
    def set_red_node(self):
        self.color = "R"
    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()

class RBT(object):#构建用于动态顺序统计的红黑树；修改插入、查询、删除等操作（维护size属性）；添加新操作：查找给定秩的元素、确定元素的秩
    def __init__(self,nodeList):
        self.nil=RBTNode(-1,color="B")
        self.root = self.nil
        for node in nodeList:
            self.RBT_insert(node)

    def os_select(self,x,order):#查找秩为i的元素 ;O(lgn)
        r=x.left.size+1
        if order==r:
            return x
        elif order<r:
            return self.os_select(order,x.left)
        else:
            return self.os_select(order-r,x.right)

    def os_rank(self,x):#确定一个元素的秩；O（lgn）
        r=x.left.size+1
        y=x #不直接用x循环是为了避免改变树原本的x结点
        while y!=self.root:
            if y==y.father.right:
                r=r+y.father.left.size+1
            y=y.father
        return r

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
        right.size=node.size #旋转后node和right的size会改变，故需更正
        node.size=node.left.size+node.right.size+1
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
        left.size = node.size  # 旋转后node和left的size会改变，故需更正
        node.size = node.left.size + node.right.size + 1
        return 1

    # 插入：从根节点开始遍历树，找node父节点的位置《红黑树的插入需调用RBT_insert_fixup（）重新着色并旋转以保证红黑树性质》
    def RBT_insert(self,node):
        cur=self.root
        father = self.nil
        while cur!=self.nil:
            cur.size = cur.size + 1  # 维护size属性
            father = cur
            if node.val<=cur.val:   #注意：值相等时插入左子树
                cur=cur.left
            else:
                cur=cur.right
        node.father = father
        if node.father==self.nil:
            self.root=node
        elif node.val<father.val:
            father.left=node
        else:
            father.right=node
        node.left=self.nil    #左右孩子指向黑色哨兵节点，以便于处理边界条件
        node.right=self.nil
        node.color="R"        #将其着色为红色
        node.size=1          #别忘了将size设为1
        self.RBT_insert_fixup(node)   #重新着色并旋转以保证红黑树性质
        #print("%d insert successfully" % node.val)
        return 1
    def RBT_insert_fixup(self,node):   #重新着色并旋转以保证红黑树性质：按node父节点是爷爷节点的左右孩子分成两类，每一类分别有三种情况
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
    def RBT_transplant(self,u,v): #用以v为根节点的子树替换以u为节点的子树
        if u.father==self.nil:
            self.root=v
        elif u==u.father.left:
            u.father.left=v
        else:
            u.father.right=v
        v.father=u.father  #这里即使v指向哨兵，也能给其父节点赋值，因此无条件语句
    def RBT_delete_fixup(self,x):#修正删除破坏的红黑树性质（主要解决黑高被破坏的问题，即x.color=="B"）
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
    def RBT_delete(self, node):  ##删除节点：
        y=node #记录要删除的结点
        y_original_color=y.color #记录要删除结点的原始颜色，用于最后检查是否破坏红黑树性质
        tmp=y.father
        if node.left ==self.nil: #   1.左子树空
            x=node.right #记录用来替换被删除结点的结点，如果经判断，需要修正删除结点后的红黑树的性质，则从该结点处开始修正
            self.RBT_transplant(node,node.right)
        elif node.right==self.nil: #   2.右子树空
            x=node.left
            self.RBT_transplant(node, node.left)
        else:     #       3.左右子树均不空：将node于其后继交换位置，并将node的颜色赋给后继，再删除后继位置上的node即可
            y=self.Tree_Minimum(node.right) #node的后继
            y_original_color=y.color
            tmp=y.father
            x=y.right
            if y.father==node: #(1) 这种情况不能直接调用transplant,会使得x.father指向node,导致RBT_delete_fixup(x)出错
                x.father=y # 注意y.right为nil时，其父节点也需指向y，否则RBT_delete_fixup(x)会出错
                tmp=node.father
            else:              #(2)
                self.RBT_transplant(y,y.right)
                y.right=node.right
                y.right.father=y
            self.RBT_transplant(node,y)
            y.left=node.left
            y.left.father=y
            y.color = node.color
            y.size=y.left.size+y.right.size+1
        while tmp!=self.nil:      #从删除位置或后继位置的父节点向上遍历结点size-1,直到根节点为止
            tmp.size=tmp.size-1
            tmp=tmp.father
        if y_original_color=="B":
            self.RBT_delete_fixup(x)
        return 1

    def RBT_to_ValColorSizeList(self):#生成二叉搜索树值的列表及颜色列表:利用队列先进先出的特性，按从上往下，从左往右的顺序排序
            if self.root==self.nil:
                print("tree is empty!")
                return -1
            ValList=[]
            ColorList=[]
            SizeList=[]
            q=queue.Queue()
            q.put(self.root)
            while q.empty() is not True: #每次从队列取出一个值放入列表，并将其左右子节点放入队列中；直到队列为空，则树的值已全部放如列表中
                node=q.get()
                ValList.append(node.val)
                ColorList.append(node.color)
                SizeList.append(node.size)
                if node.left!=self.nil:   #插入左子树
                    q.put(node.left)
                if node.right!=self.nil: #插入右子树
                    q.put(node.right)
            return ValList,ColorList,SizeList

    def search(self,val):#查询：从根节点开始搜索树，直到遇到叶子节点
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
            return -1

####################################
if __name__ == '__main__':
    node2 = RBTNode(2)
    node5 = RBTNode(5)
    node3 = RBTNode(3)
    node100=RBTNode(100)
    node10=RBTNode(10)
    node1=RBTNode(1)

    tree=RBT([node1])
    a,b,c=tree.RBT_to_ValColorSizeList()
    print(a,b,c)
    print("next")
    tree.RBT_insert(node2)
    a, b, c = tree.RBT_to_ValColorSizeList()
    print(a, b, c)
    print("next")
    tree.RBT_insert(node5)
    a, b, c = tree.RBT_to_ValColorSizeList()
    print(a, b, c)
    print("next")

    '''tree.RBT_insert(node100)
    a, b ,c= tree.RBT_to_ValColorSizeList()
    print(a, b,c)
    print("next")

    tree.RBT_delete(node1)
    a, b,c = tree.RBT_to_ValColorSizeList()
    print(a, b,c)
    print("next")

    print(tree.os_select(tree.root,2).val)
    print(tree.os_rank(tree.root))'''
