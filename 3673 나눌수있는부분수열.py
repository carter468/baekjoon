# 나눌 수 있는 부분 수열
# Gold 3, prefix sum

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    D,N = map(int,input().split())
    arr = tuple(map(int,input().split()))
    
    count = [1]+[0]*D
    x = 0
    result = 0
    for a in arr:
        x = (x+a)%D
        result += count[x]
        count[x] += 1
    print(result)