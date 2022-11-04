# 오아시스 재결합

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
answer = 0 
for h in arr:
    while stack and stack[-1][0] < h:
        answer += stack.pop()[1]
    if not stack:
        stack.append((h,1))
        continue
    if stack[-1][0] == h:
        cnt = stack.pop()[1]
        answer += cnt
        if stack:
            answer += 1
        stack.append((h,cnt+1))
    else:
        stack.append((h,1))
        answer += 1
print(answer)