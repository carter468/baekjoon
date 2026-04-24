# 고인물의 졸업 계획
# Gold 4, greedy

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
t = 0
for i in range(M):
    a = int(input())
    if a < N:
        t += a
        arr.append(i+1)
        if t >= N: break
    elif a <= N*2:
        arr = [i+1]
        break
print(len(arr),*arr,sep='\n')