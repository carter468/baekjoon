# 방사형그래프

def dfs(cnt):
    global ans
    if cnt == 8:
        ans += checkgraph()
        return
    for i in range(8):
        if visited[i]:
            continue
        visited[i] = 1
        temp[cnt] = a[i]
        dfs(cnt+1)
        visited[i] = 0

def checkgraph():
    for i in range(8):
        j = (i+1)%8
        k = (i+2)%8
        if temp[i]*temp[k]*(2**0.5) > temp[j]*(temp[i]+temp[k]):
            return 0
    return 1

a = list(map(int,input().split()))
visited = [0]*8
temp = [0]*8
ans = 0
dfs(0)
print(ans)