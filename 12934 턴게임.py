# 턴 게임

x,y = map(int,input().split())
n = int(((x+y)*2)**0.5)
if n*(n+1)//2 != x+y:
    print(-1)
else:
    cnt = 0
    while x > 0:
        x -= n
        n -= 1
        cnt += 1
    print(cnt)