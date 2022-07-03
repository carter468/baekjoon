# 가장 긴 증가하는 부분 수열 2

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = [0]

for i in A:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i
    
print (len(stack)-1)
