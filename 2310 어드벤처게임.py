# 어드벤처게임
# Gold 4, 그래프 탐색

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def adventure(idx,money):
    global answer
    if maze[idx][0] <= 0:
        money += maze[idx][0]
    else:
        money = max(money,maze[idx][0])
    if money < 0:
        return
    if idx==n:
        answer = 'Yes'
        return
    visit[idx] = True
    for now in maze[idx][1]:
        if not visit[now]:
            adventure(now,money)
    visit[idx] = False

while True:
    n = int(input())
    if n==0:
        break

    maze = [[]]
    for _ in range(n):
        a = input().split()
        if a[0] == 'T':
            maze.append((-int(a[1]),list(map(int,a[2:-1]))))
        else:
            maze.append((int(a[1]),list(map(int,a[2:-1]))))

    answer = 'No'
    visit = [False]*(n+1)
    adventure(1,0)
    print(answer)