# 해적과 보석
# Gold 2, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = 0
    for i,(a,b) in enumerate(sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:-x[0]-x[1])):
        x += -b if i%2 else a
    print(x)