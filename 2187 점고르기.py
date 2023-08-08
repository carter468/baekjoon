# 점 고르기
# Gold 5, bruteforce

import sys
input = sys.stdin.readline

n,a,b = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(i+1,n):
        if abs(arr[i][0]-arr[j][0]) < a and abs(arr[i][1]-arr[j][1]) < b:
            result = max(result,abs(arr[i][2]-arr[j][2]))
print(result)