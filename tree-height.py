'''
Problem Description
Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
Input Format. The first line contains the number of nodes π. The second line contains π integer numbers
from β1 to π β 1 β parents of nodes. If the π-th one of them (0 β€ π β€ π β 1) is β1, node π is the root,
otherwise itβs 0-based index of the parent of π-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.
Constraints. 1 β€ π β€ 105
.
Output Format. Output the height of the tree.
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time (sec) 1 1 6 3 1.5 2 5 5 3
Memory Limit. 512MB.

this programming cost 0.15s in my computer

'''

# python3
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0

                height=[0]*len(self.parent)
                nodes=list(range(self.n))
                while len(nodes)>0:
                    node=nodes.pop()
                    if self.parent[node]==-1:
                        height[node]=1
                        #print(nodes)
                    elif height[node]==0:
                        if height[self.parent[node]]==0:
                            nodes.append(node)
                            nodes.append(self.parent[node])
                            height.append(0)
                        else:
                            height[node]=height[self.parent[node]]+1
                            #print(nodes)
                #print(nodes)
                return max(height)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
