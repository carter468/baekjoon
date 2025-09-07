# Crush Fever
# Gold 3, backtracking, DFS, implementation

def touch(x,y,g):
    k = g[x][y]
    if k == 0: return 0
    g[x][y] = 0
    q = [(x,y)]
    c = 1
    while q:
        x,y = q.pop()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == k:
                g[nx][ny] = 0
                q.append((nx,ny))
                c += 1
    
    for j in range(M):
        stack = []
        for i in range(N):
            if g[i][j] != 0:
                stack.append(g[i][j])
        for i in range(N-1,-1,-1):
            if stack:
                g[i][j] = stack.pop()
            else:
                g[i][j] = 0
    
    return c*c

M,N = map(int,input().split())
arr = [input().split() for _ in range(N)]

result = 0
for a in range(N):
    for b in range(M):
        arr1 = [arr[i][:] for i in range(N)]
        c1 = touch(a,b,arr1)
        result = max(result,c1)
        for c in range(N):
            for d in range(M):
                arr2 = [arr1[i][:] for i in range(N)]
                c2 = touch(c,d,arr2)
                result = max(result,c1+c2)
                for e in range(N):
                    for f in range(M):
                        arr3 = [arr2[i][:] for i in range(N)]
                        c3 = touch(e,f,arr3)
                        result = max(result,c1+c2+c3)
print(result)