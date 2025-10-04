# Untangling Chain
# Platinum 5, constructive

import sys
input = sys.stdin.readline

N = int(input())

prev = [-1,-1]
arr = [[0,0] for _ in range(N)] # 현재 방향, 다음 방향
d = 0 # 방향 0:오 1:위 2:왼 3:아
for i in range(N):
    _,t = map(int,input().split())
    arr[i][0] = d
    arr[prev[d%2]][1] = d
    prev[d%2] = i
    d = (d+t)%4

result = []
for i in range(N):
    if arr[i][0] == arr[i][1]: # 다음 방향과 같으면 1만큼만
        result.append(1)
    else:
        result.append(max(1,N-i-1)) # 다음 방향과 다르면 길게(남은 점의 개수만큼이면 충분)
print(*result)