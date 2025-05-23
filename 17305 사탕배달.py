# 사탕 배달
# Gold 4, greedy, prefix sum

import sys
input = sys.stdin.readline

N,W = map(int,input().split())
arr1,arr2 = [],[]
for _ in range(N):
    t,s = map(int,input().split())
    if t == 3: arr1.append(s)
    else: arr2.append(s)

arr1 = [0]+sorted(arr1)[::-1]
arr2 = [0]+sorted(arr2)[::-1]
for i in range(len(arr2)-1):
    arr2[i+1] += arr2[i]
    
result = 0
x = 0
for i in range(len(arr1)):
    x += arr1[i]
    if i*3 > W: break
    result = max(result,x+arr2[min((W-i*3)//5,len(arr2)-1)])
print(result)