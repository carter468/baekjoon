# 스타트 택시
# Gold 2, 너비 우선 탐색, 구현

from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def pick(x,y):  
    if table[x][y] < 0: # 현재 위치에 손님있음
        return -table[x][y],0
    q = deque([(x,y)])
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    visit[x][y] = 0
    m = 1000
    result = []
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or table[nx][ny]==1 or visit[nx][ny]!=-1:
                continue
            if table[nx][ny]<0: # 손님
                if m>=visit[cx][cy]:    # 최단거리
                    result.append((nx,ny,-table[nx][ny]))
                    m = min(m,visit[cx][cy])
                else:   # 최단거리가 아닐시 탐색 종료
                    result.sort()
                    return result[0][2],m+1 
            visit[nx][ny] = visit[cx][cy]+1
            q.append((nx,ny))
    if result:  # 태울손님이 있다면
        result.sort()
        return result[0][2],m+1
    return -1,-1

def drive(x,y,D):
    q = deque([(x,y)])
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    visit[x][y] = 0
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or table[nx][ny]==1 or visit[nx][ny]!=-1:
                continue
            if (nx,ny) == D: # 도착
                return visit[cx][cy]+1  # 이동거리
            visit[nx][ny] = visit[cx][cy]+1
            q.append((nx,ny))
    return -1

N,M,answer = map(int,input().split())
table = []  # 지도
for _ in range(N):
    table.append(list(map(int,input().split())))
x,y = map(int,input().split())
x,y = x-1,y-1   # 택시 출발
start = [()]    # 손님 출발지
dest = [()]     # 손님 목적지
for i in range(1,M+1):
    a,b,c,d = map(int,input().split())
    start.append((a-1,b-1))
    table[a-1][b-1] = -i    # 손님 위치
    dest.append((c-1,d-1))

for _ in range(M):
    n,a = pick(x,y) # 손님 태우기
    answer -= a
    if n==-1 or answer<0:   # 못태우거나 연료부족
        answer = -1
        break
    x,y = start[n]  # 택시 위치
    table[x][y] = 0 # 손님 삭제

    a = drive(x,y,dest[n])  # 목적지 운행
    answer -= a
    if a==-1 or answer<0:   # 도착못하거나 연료부족
        answer = -1
        break
    answer += a*2   # 연료 충전
    x,y = dest[n]   # 택시 위치
    
print(answer)