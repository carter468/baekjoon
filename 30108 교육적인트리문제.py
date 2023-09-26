# 교육적인 트리 문제
# Gold 4, topological sorting, priority queue

# 위상정렬 1452ms
import heapq

n = int(input())
parent = [0]*(n+1)
indegree = [0]*(n+1)
for i,p in enumerate(map(int,input().split())):
    indegree[p] += 1
    parent[i+2] = p
arr = tuple(map(int,input().split()))

q = []
x = sum(arr)
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,(arr[i-1],i))

result = [x]
for _ in range(n-1):
    a,idx = heapq.heappop(q)
    x -= a
    result.append(x)
    px = parent[idx]
    indegree[px] -= 1
    if indegree[px] == 0:
        heapq.heappush(q,(arr[px-1],px))
            
for r in result[::-1]:
    print(r)

# 그리디 424ms

input(),input()
a = sorted(map(int,input().split()))
result = 0
while a:
    result += a.pop()
    print(result)