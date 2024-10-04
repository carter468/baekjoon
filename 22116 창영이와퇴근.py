# 창영이와 퇴근
# Gold 4, binary search, DFS

def check(c):
    q = [(0,0)]
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    while q:
        x,y = q.pop()
        if (x,y) == (n-1,n-1): return True
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and abs(arr[x][y]-arr[nx][ny]) <= c:
                visited[nx][ny] = True
                q.append((nx,ny))
    return False

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

lo,hi = -1,10**9
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
