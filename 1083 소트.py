# 소트
# Gold 5, greedy

n = int(input())
arr = list(map(int,input().split()))
s = int(input())

for i in range(n):
    m = max(arr[i:min(n,i+s+1)])
    idx = arr.index(m)
    for j in range(idx,i,-1):
        arr[j] = arr[j-1]
    arr[i] = m
    s -= idx-i
    if s == 0: break

print(*arr)