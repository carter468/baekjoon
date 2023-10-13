# 학회원
# Gold 4, DFS, hash set, parsing

import sys
input = sys.stdin.readline

while n:=int(input()):
    _,t = input().strip('.\n').split(':')
    graph = {}
    for _ in range(n-1):
        a,b = input().strip('.\n').split(':')
        graph[a] = b.split(',')

    result,visit = set(),set()
    for a in t.split(','):
        if a not in visit:
            q = [a]
            while q:
                x = q.pop()
                if x in graph:
                    for nx in graph[x]:
                        if nx not in visit:
                            visit.add(nx)
                            q.append(nx)
                else: result.add(x)

    print(len(result))