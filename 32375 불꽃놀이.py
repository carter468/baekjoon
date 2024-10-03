# 불꽃놀이
# Gold 4, two pointer

n,k = map(int,input().split())
count = 0
arr = []
for a in map(int,input().split()):
    if a >= k: count += 1
    else: arr.append(a)

arr.sort()
l,r = 0,len(arr)-1
while l < r:
    if arr[l]+arr[r] >= k:
        count += 1
        r -= 1
    l += 1
print(count if count else -1)
