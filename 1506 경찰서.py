# 경찰서
# Platinum 5, SCC

def scc(v):
    global index,result
    indices[v] = lowlink[v] = index
    index += 1
    stack.append(v)
    on_stack[v] = True

    for w in range(N):
        if arr[v][w] == '1':
            if indices[w] == -1:
                scc(w)
                lowlink[v] = min(lowlink[v],lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v],indices[w])

    if lowlink[v] == indices[v]:
        m = 10**6
        while True:
            w = stack.pop()
            on_stack[w] = False
            m = min(m,cost[w])
            if w == v:
                break
        result += m

N = int(input())
cost = tuple(map(int,input().split()))
arr = [input() for _ in range(N)]

index = 0
stack = []
indices = [-1]*N
lowlink = [0]*N
on_stack = [False]*N
result = 0
for i in range(N):
    if indices[i] == -1:
        scc(i)
print(result)