# 점프 게임
# Gold 5, DFS

def solve():
    n,k = map(int,input().split())
    line = (input(),input())

    visit = [[0]*n for _ in range(2)]
    q = [(0,0,0)]
    while q:
        x,y,t = q.pop()
        for nx,ny in (x,y+1),(x,y-1),(x^1,y+k):
            if ny >= n:
                return 1
            if ny <= t or line[nx][ny] == '0' or visit[nx][ny] == 1: continue
            q.append((nx,ny,t+1))
            visit[nx][ny] = 1
    return 0

print(solve())