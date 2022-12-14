#Uses python3
'''
Detecting Anomalies in Currency Exchange Rates

Problem Introduction

You are given a list of currencies ๐1, ๐2, . . . , ๐๐ together with a list of exchange
rates: ๐๐๐ is the number of units of currency ๐๐ that one gets for one unit of ๐๐. You 
would like to check whether it is possible to start with one unit of some currency, 
perform a sequence of exchanges, and get more than one unit of the same currency. 
In other words, you would like to find currencies ๐๐1, ๐๐2, . . . , ๐๐๐ such that
๐๐1,๐2ยท ๐๐2,๐3ยท ๐๐๐โ1,๐๐, ๐๐๐,๐1 > 1. For this, you construct the following graph: 
vertices are currencies ๐1, ๐2, . . . , ๐๐, the weight of an edge from ๐๐ to ๐๐ is equal to โ log ๐๐๐ . 
There it suffices to check whether is a negative cycle in this graph. Indeed, 
assume that a cycle ๐๐ โ ๐๐ โ ๐๐ โ ๐๐ has negative weight. This means that โ(log ๐๐๐ + log ๐๐๐ + log ๐๐๐) < 0
and hence log ๐๐๐ + log ๐๐๐ + log ๐๐๐ > 0. This, in turn, means that ๐๐๐*๐๐๐*๐๐๐ = 2^log๐๐๐ * 2^log๐๐๐ * 2^log๐๐๐ 
= 2^(log๐๐๐+log๐๐๐+log๐๐๐๏ผ > 1 .

Problem Description

Task. Given an directed graph with possibly negative edge weights and with ๐ vertices and ๐ edges, check
whether it contains a cycle of negative weight.
Input Format. A graph is given in the standard format.
Constraints. 1 โค ๐ โค 10^3, 0 โค ๐ โค 10^4, edge weights are integers of absolute value at most 10^3.
Output Format. Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
'''
import sys

def negative_cycle(adj, cost):
    #can't use inf for initialization,because the inf is not mathematically strict infinite,but a constant,so it will meet problem at line 37
    dist = [1001] * len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if  dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    # if it's the last iliteration
                    if i == len(adj) - 1:
                        return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [[] for _ in range(m)]
    for i in range(m):
        lines[i] = list(map(int, input().strip().split()))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for line in lines:
        l1 = line[0]
        l2 = line[1]
        w = line[2]
        adj[l1 - 1].append(l2 - 1)
        cost[l1 - 1].append(w)
    print(negative_cycle(adj, cost))
