# Tricknology
# Gold 4, number theory, prefix sum

import sys
input = sys.stdin.readline

M = 10**6
N = M//2

seive = [True]*M
for i in range(2,int(M**0.5)):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False

arr = [0]*N
for i in range(2,N):
    if seive[i*2+1]: arr[i] = 1
    arr[i] += arr[i-1]

for _ in range(int(input())):
    l,r = map(int,input().split())
    print(arr[r-1]-arr[l-1])