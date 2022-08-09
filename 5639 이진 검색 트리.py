# 이진 검색 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start,end):
    if start>end:
        return
    temp = end+1
    for i in range(start+1,end+1):
        if tree[start] < tree[i]:
            temp = i
            break
    dfs(start+1,temp-1)
    dfs(temp,end)
    print(tree[start])

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

dfs(0,len(tree)-1)