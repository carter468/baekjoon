# 초콜릿과 나이트 게임
# Gold 4, constructive, case work

def move():
    print(len(arr))
    x,y = 0,0
    for dx,dy in arr:
        x += dx
        y += dy
        print(x,y)

a,b = map(int,input().split())

if a == b:
    arr = (a,b),(a,-b),(a,-b),(-a,-b),(-a,-b),(-a,b),(a,b)
    move()
elif a > 0 and b > 0:
    arr = (a,b),(a,-b),(b,a),(-a,-b),(b,-a),(-b,-a),(a,-b),(-b,a),(-a,-b),(-a,b),(-b,-a),(a,b),(-b,a),(b,a),(b,-a)
    move()
else:
    if a == 0: a = b
    arr = (0,a),(a,0),(a,0),(0,-a),(0,-a),(-a,0),(0,a)
    move()