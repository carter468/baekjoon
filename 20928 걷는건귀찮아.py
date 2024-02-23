# 걷는 건 귀찮아
# Gold 4, greedy

n,m = map(int,input().split())
p = tuple(map(int,input().split()))
x = tuple(map(int,input().split()))

count = 0
e = p[0]+x[0]
i = 1
while i < n and e < m and p[i] <= e:
    temp = e
    while i < n and p[i] <= e:
        temp = max(temp,p[i]+x[i])
        i += 1
    e = temp
    count += 1
print(count if e >= m else -1)