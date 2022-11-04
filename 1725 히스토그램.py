# 히스토그램

import sys
input = sys.stdin.readline

n = int(input())
height = []
for _ in range(n):
    height.append(int(input()))
height.append(0)

answer = 0
stack = [-1]
for i in range(n+1):
    while stack and height[stack[-1]] > height[i]:
        h = height[stack.pop()]
        w = i-stack[-1]-1
        answer = max(answer,h*w)
    stack.append(i)

print(answer)