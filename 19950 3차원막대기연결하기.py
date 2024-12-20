# 3차원 막대기 연결하기
# Gold 4, geometry

x1,y1,z1,x2,y2,z2 = map(int,input().split())
input()
arr = tuple(map(int,input().split()))

d = (x1-x2)**2+(y1-y2)**2+(z1-z2)**2
a,b = sum(arr),max(arr)
print('YES' if max(0,b-(a-b))**2 <= d <= a**2 else 'NO')