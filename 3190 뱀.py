# 뱀
# Gold 4, 덱

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
apple = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    apple[a][b] = 1
rotation = ['']*10001
for _ in range(int(input())):
    a,b = input().split()
    rotation[int(a)] = b

snake = deque([[1,1]])
rotate_table = [[0,1],[1,0],[0,-1],[-1,0]]  # 우 하 좌 상
direction = 0
x = 0
while True:
    x += 1
    i,j = snake[-1][0]+rotate_table[direction][0], snake[-1][1]+rotate_table[direction][1]
    if 1>i or n<i or 1>j or n<j or [i,j] in snake:
        print(x)
        break
    if not apple[i][j]:
        snake.popleft()
    snake.append([i,j])
    apple[i][j] = 0
    if rotation[x] == 'D':
        direction = (direction+1)%4
    elif rotation[x] == 'L':
        direction = (direction-1)%4