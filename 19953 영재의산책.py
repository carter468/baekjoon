# 영재의 산책
# Gold 4, number theory

V,M,T = map(int,input().split())

v = V
arr = []
for i in range(4):
    v = v*M%10
    arr.append(v)

a,b = divmod(T-1,4)
count = [a]*4
for i in range(b):
    count[i] += 1

x,y = 0,V
for i in range(4):
    x += count[i]*arr[i]*[1,0,-1,0][i]
    y += count[i]*arr[i]*[0,-1,0,1][i]
print(x,y)