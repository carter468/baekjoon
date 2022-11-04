# 히스토그램

import sys
input = sys.stdin.readline

n = int(input())
height = [0]*(n+1)
for i in range(n):
    height[i] = int(input())

answer = 0
stack = []
for i in range(n):
    left = i
    while stack and height[stack[-1]] > height[i]:
        h = height[stack[-1]]
        stack.pop()
        w = i
        if stack:
            w -= stack[-1]+1
        answer = max(answer,h*w)
    stack.append(i)

while stack:
    h = height[stack[-1]]
    stack.pop()
    w = n
    if stack:
        w -= stack[-1]+1
    answer = max(answer,h*w)

print(answer)