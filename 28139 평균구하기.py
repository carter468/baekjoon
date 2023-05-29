# 평균 구하기
# Gold 4, 수학

import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(i+1,n):
        result += ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**0.5

print(result*2/n)