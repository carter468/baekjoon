# 색종이

import sys
input = sys.stdin.readline

colorpaper = [[0]*100 for _ in range(100)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            colorpaper[i][j] = 1

area_black = 0
for row in colorpaper:
    area_black += row.count(1)
print(area_black)