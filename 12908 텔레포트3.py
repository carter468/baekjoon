# 텔레포트 3
# Gold 5, bruteforcing

def move(x,y,dist):
    global result
    result = min(result,dist+abs(x-xe)+abs(y-ye))
    for i in range(3):
        if not visited[i]:
            visited[i] = True
            x1,y1,x2,y2 = arr[i]
            move(x1,y1,dist+abs(x-x2)+abs(y-y2)+10)
            move(x2,y2,dist+abs(x-x1)+abs(y-y1)+10)
            visited[i] = False

xs,ys = map(int,input().split())
xe,ye = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(3)]

visited = [False]*3
result = 10**10
move(xs,ys,0)
print(result)