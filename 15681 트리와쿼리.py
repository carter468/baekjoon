# 트리와 쿼리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def maketree(currentNode,parent):
    for x in connect[currentNode]:
        if x != parent:
            child[currentNode].append(x)
            maketree(x,currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for x in child[currentNode]:
        countSubtreeNodes(x)
        size[currentNode] += size[x]

n,r,q = map(int,input().split())
connect = [[] for _ in range(n+1)]
child = [[] for _ in range(n+1)]
size = [0]*(n+1)
for _ in range(n-1):
    u,v = map(int,input().split())
    connect[u].append(v)
    connect[v].append(u)

maketree(r,-1)
countSubtreeNodes(r)

for _ in range(q):
    u = int(input())
    print(size[u])