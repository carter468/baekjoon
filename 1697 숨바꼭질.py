# 숨바꼭질

n,k = map(int,input().split())

def bfs(i):
    global k
    visited[i] = 1
    q = [i]
    while q:
        x = q.pop(0)
        a = x+1
        b = x-1
        c = x*2
        if a<len(visited) and visited[a]==0:
            visited[a] = visited[x] + 1
            q.append(a)
        if b>=0 and visited[b]==0:
            visited[b] = visited[x] + 1
            q.append(b)
        if c<len(visited) and visited[c]==0:
            visited[c] = visited[x] + 1
            q.append(c)
        if a==k:
            print(visited[a]-1)
            return
        if b==k:
            print(visited[b]-1)
            return
        if c==k:
            print(visited[c]-1)
            return
            
visited = [0]*200000
bfs(n)