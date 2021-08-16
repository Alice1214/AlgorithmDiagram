# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: 打印所有决策路径（假设决策树的分支最多有三个）
# Author:  HuiHui
# Date:    2019-03-10
# Reference: https://segmentfault.com/q/1010000009355715
#################################
import copy
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left,self.mid,self.right = None,None,None

def get_path(node, result, tmp=[]):
    if node is None:
        return
    tmp.append(node)
    tmp1 = copy.deepcopy(tmp) #deepcopy深度拷贝，内存地址完全不同，修改tmp不会影响tmp1;若直接用=赋值，列表元的内存地址是一样的，因此当tmp or tmp1有修改时另一方也会有同样的修改。
    tmp2 = copy.deepcopy(tmp)

    if node.left is None and node.mid is None and node.right is None: #叶子节点
        result.append([i.val for i in tmp])
        return

    if node.left is not None:
        get_path(node.left, result, tmp)
    if node.mid is not None:
        get_path(node.mid, result, tmp1)
    if node.right is not None:
        get_path(node.right, result, tmp2)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.mid=node5
    node2.right=node6
    node3.left = node7

    r = []
    get_path(node1, result=r)
    print(r)
