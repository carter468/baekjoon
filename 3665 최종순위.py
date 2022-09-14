# 최종순위

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    t = list(map(int,input().split()))  # 작년 순위
    graph = [[] for _ in range(n+1)]    # 나보다 순위가 낮은 팀을 원소로 갖는 배열
    indegree = [0]*(n+1)                # 진입차수
    for i in range(n-1):
        for j in range(i+1,n):
            graph[t[i]].append(t[j])   
            indegree[t[j]] += 1
    
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1

    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    result = True
    ans = []
    if not q:
        result = False
    while q:
        if len(q) >= 2:
            result = False
            break
        a = q.popleft()
        ans.append(a)
        for i in graph[a]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            elif indegree[i] < 0:
                result = False
                break
    
    if result == False or len(ans) < n:
        print('IMPOSSIBLE')
    else:
        print(*ans)