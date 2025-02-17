# 로봇 조립
# Gold 4, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M = 10**6+1

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

root = list(range(M))
count = [1]*M
for _ in range(int(input())):
    q,*arr = input().split()
    if q == 'I':
        a,b = map(find,map(int,arr))
        if a != b:
            root[a] = b
            count[b] += count[a]
    else:
        print(count[find(int(arr[0]))])