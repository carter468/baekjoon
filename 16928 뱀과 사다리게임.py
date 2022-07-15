# 뱀과 사다리게임

from collections import deque

n,m = map(int,input().split())  
board = [0] * 101                # 게임판
visited = [0] * 101             # 방문기록
for _ in range(n+m):
    a,b = map(int,input().split())
    board[a] = b                 # 뱀과 사다리 정보 

def bfs():
    visited[1] = 1              # 0번 굴렸을때 1이므로 마지막에 1 빼주기
    q = deque([1])

    while q:
        x = q.popleft()

        for i in range(1,7):   # 1~6 주사위 굴리기 
            nx = x+i            
            if nx<101:
                if board[nx] != 0:      # 뱀 또는 사다리 조우
                    nx = board[nx]
                if visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
                
            if nx == 100:           # 도착
                return visited[nx]-1

print(bfs())