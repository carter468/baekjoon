# Circular Barn (Gold)
# Platinum 4, greedy

from collections import deque
import sys
input = sys.stdin.readline

A = [int(input()) for _ in range(int(input()))]

s = 10**9,0
c = 0
for i,a in enumerate(A):
    c += a-1
    if c < s[0]: s = c,i
s = s[1]+1

q = deque()
result = 0
for i,a in enumerate(A[s:]+A[:s]):
    q.extend([i]*a)
    j = q.popleft()
    result += (i-j)**2
print(result)