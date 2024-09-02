# 캠프 준비
# Gold 5, bruteforcing

n,l,r,x = map(int,input().split())
arr = tuple(map(int,input().split()))

count = 0
for i in range(1<<n):
    c = 0
    p = []
    for j in range(n):
        if i>>j&1:
            c += 1
            p.append(arr[j])
    if c > 1 and l <= sum(p) <= r and max(p)-min(p) >= x: count += 1
print(count)
