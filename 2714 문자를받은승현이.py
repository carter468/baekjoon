# 문자를 받은 승현이

import sys
input = sys.stdin.readline

def check(a,b,r,c):
    if 0<=a<=r-1 and 0<=b<=c-1 and msg1[a][b] != -1:
        return True
    return False

def change(x):
    y = 0
    for i in range(5):
        y += int(x[i])*(2**(4-i))
    if y==0:
        y = -32
    return chr(y+64)

t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(t):
    r,c,msg = map(str,input().split())
    r,c = map(int,[r,c])
    msg1 = [[0 for _ in range(c)] for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c):
            msg1[i][j] = msg[cnt]
            cnt += 1

    cnt = 1
    tmp = ''
    result = []
    x,y = 0,0
    d = 0
    while cnt <= len(msg):
        tmp += msg1[x][y]
        msg1[x][y] = -1
        if len(tmp) == 5:
            result.append(tmp)
            tmp = ''
        a = x+dx[d]
        b = y+dy[d]
        if check(a,b,r,c):  # 다음 좌표
            x = a
            y = b
        else:
            d = (d+1)%4
            x += dx[d]
            y += dy[d]
        cnt += 1

    ans = ''
    for alphabet in result:
        ans += change(alphabet)
    print(ans.rstrip())