# 다음 순열

def solve(l):
    if l == n:
        print(*arr)
        quit()
    for i in range(1,n+1):
        if visited[i] == False:
            arr.append(i)
            visited[i] = True
            solve(l+1)
            
n = int(input())
arr = list(map(int,input().split()))
visited = [True]*(n+1)
visited[arr[-1]] = False
arr.pop()
while len(arr) > 0:
    for i in range(arr[-1],n+1):
        if visited[i] == False:
            visited[arr[-1]] = False
            visited[i] = True
            arr[-1] = i
            solve(len(arr))
    visited[arr[-1]] = False
    arr.pop()
print(-1)