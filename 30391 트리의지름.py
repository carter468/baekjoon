# 트리의 지름?
# Gold 4, constructive

n,k = map(int,input().split())

c = [0]*(n+1)
prev = 1
for i in range(2,n+1):
    print(prev,i)
    c[prev] += 1
    c[i] += 1
    while c[prev] == k:
        prev += 1