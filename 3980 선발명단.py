# 선발명단
# Gold 5, 백트래킹

import sys
input = sys.stdin.readline

def solve(n,score):
    global answer
    if n==11:
        answer = max(answer,score)
        return
    
    for i in range(11):
        if player[n][i] and not position[i]:
            position[i] = 1
            solve(n+1,score+player[n][i])
            position[i] = 0

for _ in range(int(input())):
    player = [tuple(map(int,input().split())) for _ in range(11)]
    position = [0]*11
    answer = 0
    solve(0,0)
    print(answer)