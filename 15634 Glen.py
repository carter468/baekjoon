# Glen
# Platinum 5, constructive, implementation

def toggle(x,y):
    arr[x][y] ^= 1

N,M = map(int,input().split())
T = [input() for _ in range(N)]

arr = [[0]*(M+1) for _ in range(N+1)]
toggle(0,0)
result = ['R']
for x in range(N):
    if x%2 == 0:
        for y in range(M):
            if '.#'[arr[x][y]] != T[x][y]:
                result.append('RL')
            else:
                toggle(x,y+1)
            if y < M-1: result.append('R')
    else:
        for y in range(M-1,-1,-1):
            if '.#'[arr[x][y]] != T[x][y]:
                result.append('LR')
            else:
                toggle(x,y-1)
            if y > 0: result.append('L')
    result.append('D')
    toggle(x+1,y)
print(''.join(result[:-1]))