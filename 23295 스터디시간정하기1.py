# 스터디 시간 정하기 1
# Gold 3, prefix sum, sliding window

import sys
input = sys.stdin.readline

M = 10**5+1
n,t = map(int,input().split())
arr = [0]*M
for _ in range(n):
    for _ in range(int(input())):
        s,e = map(int,input().split())
        arr[s] += 1
        arr[e] -= 1

for i in range(M-1):
    arr[i+1] += arr[i]

x = sum(arr[1:t+1])
result = [x,t]
for i in range(t+1,M):
    x += arr[i]-arr[i-t]
    if x > result[0]:
        result = [x,i+1]
print(result[1]-t,result[1])