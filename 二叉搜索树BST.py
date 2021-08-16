# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: BST查询、插入、删除
# Author:  HuiHui
# Date:    2019-04-30
# Reference:  https://www.cnblogs.com/lilip/p/9937697.html
#################################
import queue


class TreeNode(object):#定义节点类
    def __init__(self, val):
        self.val = val
        self.left,self.right,self.father = None,None,None


class BST(object):#定义二叉搜索树及构建、插入、查询、删除等方法
    def __init__(self,nodeList):
        self.root = None
        for node in nodeList:#nodeList是节点组成的列表，逐个插入节点，构建BST
            self.insert(node)

    def insert(self,node):#插入：从根节点开始遍历树，找node父节点的位置
            cur=self.root#存放当前遍历到的节点
            father = None#存放node的父节点
            while cur!=None:           #找到一个空的位置来插入node
                father = cur
                if node.val<cur.val:   #插入左子树
                    cur=cur.left
                elif node.val>cur.val: #插入右子树
                    cur=cur.right
                else:                  #值相等，则插入失败
                    print("%d is already in Tree" % node.val)
                    return -1
            node.father = father  # node的父节点
            if node.father==None: #表明树是空的
                self.root=node
            elif node.val<father.val:
                father.left=node
            else:
                father.right=node
            #print("%d insert successfully" % node.val)
            return 1

    def BST_to_ValList(self):#生成二叉搜索树值的列表:利用队列先进先出的特性，按从上往下，从左往右的顺序排序
            if self.root==None:
                print("tree is empty!")
                return -1
            ValList=[]
            q=queue.Queue()
            q.put(self.root)
            while q.empty() is not True: #每次从队列取出一个值放入列表，并将其左右子节点放入队列中；直到队列为空，则树的值已全部放如列表中
                node=q.get()
                ValList.append(node.val)
                if node.left!=None:   #插入左子树
                    q.put(node.left)
                if node.right!=None: #插入右子树
                    q.put(node.right)
            return ValList

    def search(self,val):#查询：从根节点开始搜索树，直到遇到叶子节点
            if self.root==None:
                print("tree is empty!")
                return -1
            cur=self.root   #存放当前遍历到的节点
            while cur!=None:
                if val==cur.val:  #找到了val
                    print("%d is found" % val)
                    return cur
                elif val>cur.val:
                    cur=cur.right
                else:
                    cur=cur.left
            print("%d is not in tree" % val)
            return None

    def delete(self, node): ##删除节点：按节点左子树是否为空分情况考虑
        father = node.father        #存放被删节点的父节点

        ## 1.node的左子树为空
        if node.left==None:
            if father==None:                    #（1）node为根节点
                self.root=node.right
                if node.right!=None:    #且右子节点非空
                    node.right.father=None
            elif father.left==node:             #（2）node有父节点，且为其父节点的左子节点
                father.left=node.right
                if node.right!=None:    #且右子节点非空,则其父节点变成father
                    node.right.father=father
            else:                               # （2）node有父节点，且为其父节点的右子节点
                father.right = node.right
                if node.right!=None:
                    node.right.father=father
            return 'delete successfully'

        ## 2.node的左子树非空
        ##将node的右子树挂到其左子树最右的子节点下（这样挪动使得删除node时，直接把左子树挪到node父节点下即可，其原理时右
          #子树比左子树所有节点值都大，如果将右子树并到node左子节点下，必然是在在最右边，即最大值的位置）
        tmpNode=node.left
        while tmpNode.right!=None:  #找到最右子节点
            tmpNode=tmpNode.right
        tmpNode.right=node.right    #将右子树挂到最右子节点右边
        if node.right!=None:
            node.right.father=tmpNode
          #删除node
        if father == None:            # （1）node为根节点
            self.root = node.left
            node.left.father = None
        elif father.left == node:     # （2）node有父节点，且为其父节点的左子节点
            father.left = node.left
            node.left.father = father
        else:                         # （2）node有父节点，且为其父节点的右子节点
            father.right = node.left
            node.left.father = father
        return 'delete successfully'

####################################
if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(5)
    tree=BST([node1])
    tree2=BST([])

    tree.insert(node2)
    print(tree.root.right.val)
    print(tree.root.val)
    tree.insert(node2)
    tree.insert(TreeNode(7))
    tree.insert(TreeNode(1))

    a=tree.BST_to_ValList()
    print(a)

    b=tree.search(7)
    b2=tree2.search(7)
    print(b.val)

    node=tree.root.left
    tree.delete(node)
    tree.delete(tree.root)
    print(tree.BST_to_ValList())