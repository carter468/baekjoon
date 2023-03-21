# 대피소 찾기
# Gold 1, 선분 교차 판정

import sys
input = sys.stdin.readline

def ccw(a,b,c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[0]*c[1] - c[0]*b[1] - b[0]*a[1]

def clash(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            x = robot[i]
            y = shelter[int(a[i])]
            z = robot[j]
            w = shelter[int(a[j])]
            xyz = ccw(x,y,z)
            xyw = ccw(x,y,w)
            zwx = ccw(z,w,x)
            zwy = ccw(z,w,y)
            if xyz*xyw == 0 and zwx*zwy == 0:
                if min(x[0],y[0]) <= max(z[0],w[0]) and min(z[0],w[0]) <= max(x[0],y[0]) and min(x[1],y[1]) <= max(z[1],w[1]) and min(z[1],w[1]) <= max(x[1],y[1]):
                    return True
            elif xyz*xyw <= 0 and zwx*zwy <= 0:
                return True
    return False

def bt(c,a):
    if clash(a): return 0
    if c == n:
        return a
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            if (result := bt(c + 1, a + str(i))): return result
            visit[i] = 0

n = int(input())
robot = [list(map(int,input().split())) for _ in range(n)]
shelter = [list(map(int,input().split())) for _ in range(n)]
visit = [0]*n
result = bt(0,'')
for i in result:
    print(int(i) + 1)