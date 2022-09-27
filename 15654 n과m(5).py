# N과M (5)

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []
visited = [False]*n

def solve(k):
    if k==m:
        print(*ans)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(a[i])
            solve(k+1)
            ans.pop()
            visited[i] = False

solve(0)