# 꼼꼼한 쿠기의 졸업여행
# Platinum 4, offline queries, disjoint set

# pypy 메모리초과로 python3 제출
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
lst = [int(input()) for _ in range(N)]

root = list(range(N+1))
result = [False]
c = 0
check = [False]*(N+1)
for i,x in enumerate(lst[::-1]):
    check[x] = True
    for nx in graph[x]:
        if check[nx]:
            a,b = find(x),find(nx)
            if a != b: c += 1
            root[b] = a
    result.append(c==i)

for r in result[::-1]:
    print(['DIS',''][r]+'CONNECT')

# 메모리 개선 pypy제출
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
lst = [int(input()) for _ in range(N)][::-1]

root = list(range(N+1))
result = [False]
c = 0
check = [False]*(N+1)
for i,x in enumerate(lst):
    check[x] = True
    for nx in graph[x]:
        if check[nx]:
            a,b = find(x),find(nx)
            if a != b: c += 1
            root[b] = a
    result.append(c==i)

for i in range(N,-1,-1):
    print(['DIS',''][result[i]]+'CONNECT')