# 모독
# Gold 5, 그리디 알고리즘

import sys
input = sys.stdin.readline

N = int(input())
hs = sorted([int(input()) for _ in range(N)])
answer = hs[0]-1
hs[0] = 1

for i in range(N-1):
    if hs[i+1]!=hs[i]:
        answer += hs[i+1]-hs[i]-1
        hs[i+1] = hs[i]+1

print(answer)