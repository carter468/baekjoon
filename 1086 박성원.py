# 박성원

import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(input())
k = int(input())

def dfs(cnt):
    if cnt == n:
        if 