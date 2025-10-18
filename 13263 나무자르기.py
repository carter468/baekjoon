# 나무 자르기
# Platinum 2, CHT

from collections import deque

def intersect(l1,l2):
    a1,b1 = l1
    a2,b2 = l2
    return (b2-b1)/(a1-a2)

def add_line(a,b):
    while len(stack) >= 2 and intersect(stack[-2],stack[-1]) > intersect(stack[-1],(a,b)):
        stack.pop()
    stack.append((a,b))

def query(x):
    while len(stack) >= 2 and stack[0][0]*x+stack[0][1] > stack[1][0]*x+stack[1][1]:
        stack.popleft()
    a,b = stack[0]
    return a*x+b

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

stack = deque()
dp = [0]*N

add_line(B[0],dp[0])
for i in range(1,N):
    dp[i] = query(A[i])
    add_line(B[i],dp[i])

print(dp[-1])