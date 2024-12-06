# Noisy Neighbors (Large)
# Gold 2, greedy

import sys
input = sys.stdin.readline

def solve(idx):
    result,remaining = 0,R*C-N
    for i in range(4,0,-1):
        x = min(remaining,count[idx][i])
        result += i*x
        remaining -= x
    return result

for t in range(int(input())):
    R,C,N = map(int,input().split())
    answer = 0
    if N*2 > R*C:
        count = [[0]*5 for _ in range(2)]
        for i in range(R):
            for j in range(C):
                c = 0
                for ni,nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0 <= ni < R and 0 <= nj < C: 
                        c += 1
                count[(i+j)%2][c] += 1
        answer = R*(C-1)+(R-1)*C-max(solve(0),solve(1))
    
    print(f'Case #{t+1}: {answer}')