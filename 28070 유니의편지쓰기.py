# 유니의 편지 쓰기
# Gold 5, prefix sum, IMOS

import sys
input = sys.stdin.readline
M = 10**6

arr = [0]*M
for _ in range(int(input())):
    a,b = input().split()
    a = int(a[:4]+a[5:])
    b = int(b[:4]+b[5:])
    arr[a] += 1
    arr[b+1] -= 1

for i in range(200001,M-1):
    arr[i+1] += arr[i]

result = 0
answer = 0
for i in range(200001,M):
    if arr[i] > result:
        result = arr[i]
        answer = i
answer = str(answer)
print(answer[:4]+'-'+answer[4:])