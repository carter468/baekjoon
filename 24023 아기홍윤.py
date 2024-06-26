# 아기 홍윤
# Gold 5, greedy, bitmask

n,k = map(int,input().split())
arr = tuple(map(int,input().split()))

x = 0
s = 0
for i in range(n):
    if k|arr[i] > k:
        x = 0
        s = i+1
        continue
    x |= arr[i]
    if x == k:
        print(s+1,i+1)
        break
else:
    print(-1)