# 숨바꼭질 4

n,k = map(int,input().split())

def bfs(i):
    q = [i]
    while q:
        x = q.pop(0)
        if x == k:
            print(visited[x])
            return
        for i in (x+1,x-1,x*2):
            if 0<=i<=100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
                p[i] = x
            
visited = [0]*100001
p = [0]*100001  # 방문추적
bfs(n)

ans = []
while k != n:
    ans.append(k)
    k = p[k]
ans.append(n)
print(*reversed(ans))