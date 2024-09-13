# 나도리팡
# Gold 5, greedy, two pointer

n,k,t = map(int,input().split())
arr = sorted(map(int,input().split()))

count = 0
l,r = 0,n-1
while l < r:
    a = arr[l]+arr[r]
    if a > k:
        count += k-arr[r]
        arr[l],arr[r] = a-k,0
        r -= 1
    elif a == k:
        count += arr[l]
        arr[l],arr[r] = 0,0
        l += 1
        r -= 1
    else:
        count += arr[l]
        arr[l],arr[r] = 0,a
        l += 1
if sum(arr) == 0 and count <= t: print('YES')
else: print('NO')
