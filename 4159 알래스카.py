# 알래스카
# Silver 3

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n==0:
        break
    array = []
    for _ in range(n):
        array.append(int(input()))
    array.sort()
    answer = 'POSSIBLE'
    for i in range(1,n):
        if array[i]-array[i-1] > 200:
            answer = 'IMPOSSIBLE'
            break
    if array[-1] < 1322:
        answer = 'IMPOSSIBLE'
    print(answer)