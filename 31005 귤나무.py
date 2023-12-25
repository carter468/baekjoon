# 귤나무
# Gold 1, math, simulation

n,m = map(int,input().split())
arr = tuple(map(int,input().split()))

m %= sum(arr)
while arr:
    temp = []
    t = 0
    for a in arr:
        if a <= m:
            m -= a
            temp.append(a)
            t += a
    if t: m %= t
    arr = temp
print(m)