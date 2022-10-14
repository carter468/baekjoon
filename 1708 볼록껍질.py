# 볼록껍질

import sys
input = sys.stdin.readline

n = int(input())
answer = -2
coordinate = []
for _ in range(n):
    coordinate.append(list(map(int,input().split())))
coordinate.sort(key=lambda x:(x[0],x[1]))

