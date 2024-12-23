# 팬이에요
# Gold 3, math, geometry

import sys,math
input = sys.stdin.readline

def calculate(x1,y1,x2,y2):
    return (math.degrees(math.atan2(y1,x1))-math.degrees(math.atan2(y2,x2)))%360

m = 0
arr = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    d = x*x+y*y
    if d == m:
        arr.append((x,y))
    elif d > m:
        m = d
        arr = [(x,y)]

result = 0
for i in range(len(arr)):
    result = max(result,calculate(arr[i][0],arr[i][1],arr[i-1][0],arr[i-1][1]))
if result == 0: result = 360
print(result)