# 루트 게임
# Gold 5, DP, game theory

import sys
input = sys.stdin.readline

M = 10**6+1

win = [0]*M
win[1] = 1
for i in range(2,10**6):
    if i*i < M: win[i*i] = 1
    if win[i] == 0:
        j = 1
        while i+j*j < M:
            win[i+j*j] = 1
            j += 1

for _ in range(int(input())):
    print(('cubelover','koosaga')[win[int(input())]])