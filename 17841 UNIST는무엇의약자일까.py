# UNIST는 무엇의 약자일까?
# Gold 3, DP

import sys
input = sys.stdin.readline
MOD = 10**9+7
S = 'UNIST'

count = [1]+[0]*5
for _ in range(int(input())):
    w = input()
    n = len(w)
    
    for i in range(5):
        if w[0] == S[i]: break
    
    for j in range(5):
        if j >= n or i+j >= 5 or w[j] != S[i+j]: break
        count[i+j+1] = (count[i+j+1]+count[i])%MOD

print(count[5])