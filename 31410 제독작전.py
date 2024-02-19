# 제독 작전
# Gold 3, greedy, prefix sum

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(n)])
m = sys.maxsize

t1 = 0
for i in range(n):
    t1 += arr[i][1]

t2,t3 = 0,0
for i in range(n):
    t2 += abs(arr[i][0]-arr[0][0])
for i in range(1,n):
    m = min(m,t1+t2-arr[i][1]-abs(arr[i][0]-arr[0][0]))
    t3 += abs(arr[i][0]-arr[1][0])
m = min(m,t1+t3-arr[0][1])

arr.reverse()
t4,t5 = 0,0
for i in range(n):
    t4 += abs(arr[0][0]-arr[i][0])
for i in range(1,n):
    m = min(m,t1+t4-arr[i][1]-abs(arr[0][0]-arr[i][0]))
    t5 += abs(arr[i][0]-arr[1][0])
m = min(m,t1+t5-arr[0][1])

print(m)