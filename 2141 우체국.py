# 우체국
# Gold 4, greedy

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

c = 0
for x,a in arr:
    c += a

k = 0
for x,a in arr:
    k += a
    if k*2 >= c:
        print(x)
        break