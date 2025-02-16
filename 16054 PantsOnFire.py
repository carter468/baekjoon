# Pants On Fire
# Gold 5, DFS

from collections import defaultdict

def solve():
    def check(g):
        q = [a]
        visited = {a}
        while q:
            x = q.pop()
            if x == b:
                return True
            for nx in g[x]:
                if nx not in visited:
                    visited.add(nx)
                    q.append(nx)

    a,*_,b = input().split()
    if check(graph): return 'Fact'
    if check(graph_r): return 'Alternative Fact'
    return 'Pants on Fire'

N,M = map(int,input().split())

graph = defaultdict(list)
graph_r = defaultdict(list)
for _ in range(N):
    a,*_,b = input().split()
    graph[a].append(b)
    graph_r[b].append(a)

for _ in range(M):
    print(solve())