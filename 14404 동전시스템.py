# 동전 시스템
# Gold 4, number theory, DFS

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def dfs(a,b):
    visited = [False]*M
    visited[0] = True
    q = [0]
    while q:
        x = q.pop()
        for nx in (x+a,x+b):
            if nx < M and not visited[nx]:
                visited[nx] = True
                q.append(nx)
    return visited

A,B,X = map(int,input().split())

if gcd(A,B)%X == 0:
    print(-1)
else:
    M = 40001
    count = 0
    v1 = dfs(A,B)
    for y in range(1,max(A,B)+1):
        if gcd(A,B)%gcd(X,y) != 0: continue
        v2 = dfs(X,y)
        for i in range(M):
            if v1[i] and not v2[i]:
                break
        else:
            count += 1
    print(count)