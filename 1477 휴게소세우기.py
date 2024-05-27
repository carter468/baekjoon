# 휴게소 세우기
# Gold 4, binary search

n,m,l = map(int,input().split())
arr = [0]+sorted(map(int,input().split()))+[l]

lo,hi = 0,l
while lo+1 < hi:
    mid = (lo+hi)//2
    count = 0
    for i in range(n+1):
        count += (arr[i+1]-arr[i]-1)//mid
    if count <= m: hi = mid
    else: lo = mid
print(hi)