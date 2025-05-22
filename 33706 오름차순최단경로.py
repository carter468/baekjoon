# 오름차순 최단 경로
# Gold 4, greedy

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
check = [False]*N
check[0] = True
for _ in range(M):
    check[max(map(int,input().split()))-1] = True
print('YES' if all(check) else 'NO')