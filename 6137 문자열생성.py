# 문자열 생성
# Gold 4, greedy, two pointer

import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

result = []
l,r = 0,n-1
while l <= r:
    if arr[l] == arr[r]:
        ll,rr = l+1,r-1
        while ll <= rr:
            if arr[ll] < arr[rr]:
                result.append(arr[l])
                l += 1
                break
            elif arr[ll] > arr[rr]:
                result.append(arr[r])
                r -= 1
                break
            else:
                ll += 1
                rr -= 1
        else:
            result.append(arr[l])
            l += 1
    elif arr[l] < arr[r]:
        result.append(arr[l])
        l += 1
    else:
        result.append(arr[r])
        r -= 1
    
for i in range(len(result)):
    print(result[i],end='')
    if (i+1)%80 == 0: print()