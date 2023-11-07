# 현수막 걸기
# Gold 5, binary search

n,m,r = map(int,input().split())
arr = tuple(map(int,input().split()))
height = tuple(map(int,input().split()))

length = set()
for i in range(n):
    for j in range(i+1,n):
        length.add(abs(arr[i]-arr[j]))
length = sorted(length)

result = 0
for h in height:
    if h*length[0]/2 > r: continue
    lo,hi = -1,len(length)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if h*length[mid]/2 <= r: lo = mid
        else: hi = mid
    result = max(result,h*length[lo]/2)
print(f'{result:.1f}' if result else -1)