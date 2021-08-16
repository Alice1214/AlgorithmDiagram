# !/usr/bin/env python
# -*- coding=utf-8 -*-
# Summary: Dijkstra算法（解决带权重的有向图单源最短路径问题；要求权重非负无环；思路：贪心策略，不断将能最短到达的节点u加入集合S,并松弛从u出发的边）(时间O(n2))
# Author:  HuiHui
# Date:    2019-09-20
# Reference:
#################################
# graph:邻接矩阵存储带权有向图(利用字典构造二维散列表，values为权重)；s:源点（节点名）
# cost:存储源点到各点的最短路径估计（散列表）;path:存储前驱节点（散列表）
# S集合：已找到最短路径的节点集合（列表）

def find_lowest_cost_node(costs,S): # 在未处理的节点中找开销最小的节点
    lowest_cost_node=None
    lowest_cost=float("inf")
    for node in costs.keys():
        cost=costs[node]
        if cost<lowest_cost and node not in S:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra(graph, s):
    if graph == None:
        return None

    # 获取所有节点
    V=graph.keys()

    costs = {}
    path = {}
    infinity=float("inf")

    #初始化cost和path
    for key in V:
        if key==s:
            costs[key]=0
        else:
            costs[key]=infinity
        path[key]=None

    S=[]#存储处理过的节点 ,即已找到最短路径的节点
    node=find_lowest_cost_node(costs,S)#在未处理的节点中找开销最小的节点
    while node is not None:#只要还有未处理的节点，则执行
        cost=costs[node]
        neighbors=graph[node]

        # 松弛所有从node出发的边
        for key in neighbors.keys():
            if costs[key]>cost+neighbors[key]: #key从node通过最短路径更小，更新cost和path
                costs[key]=cost+neighbors[key]
                path[key]=node

        S.append(node)#标记node为处理过的
        node = find_lowest_cost_node(costs,S)#找出接下来要处理的节点
    return costs,path


####################################
if __name__ == '__main__':
    graph={"O":{"A":6,"B":2},"A":{"F":1},"B":{"A":3,"F":5},"F":{}}
    s="O"
    costs,path=dijkstra(graph, s)
    print(costs)
    print(path)

