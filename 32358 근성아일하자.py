# 근성아 일하자
# Gold 5, two pointer

import sys
input = sys.stdin.readline

dist,x = 0,0
arr = set()
for _ in range(int(input())):
    query = input().split()
    if query[0] == '1':
        arr.add(int(query[1]))
    else:
        n = len(arr)
        arr = sorted(arr)
        for i in range(n):
            if arr[i] >= x:
                l,r = i-1,i
                break
        else: l,r = n-1,n
        
        while 0 <= l or r < n:
            if l < 0:
                dist += abs(arr[r]-x)
                x = arr[r]
                r += 1
            elif r >= n:
                dist += abs(x-arr[l])
                x = arr[l]
                l -= 1
            else:
                if abs(x-arr[l]) <= abs(arr[r]-x):
                    dist += abs(x-arr[l])
                    x = arr[l]
                    l -= 1
                else:
                    dist += abs(arr[r]-x)
                    x = arr[r]
                    r += 1
        arr = set()
print(dist)