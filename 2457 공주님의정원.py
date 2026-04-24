# 공주님의 정원
# Gold 3, greedy

import sys
input = sys.stdin.readline
M = [0,31,28,31,30,31,30,31,31,30,31,30]

def f(m,d):
    return sum(M[:m])+d

S,E = f(3,1),f(11,30)
arr = []
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    x,y = f(a,b),f(c,d)
    if y > S: arr.append((x,y))
arr.sort()

N = len(arr)
count = 0
i = 0
p = S
while i < N and p <= E:
    m = 0
    count += 1
    while i < N and arr[i][0] <= p:
        m = max(m,arr[i][1])
        i += 1
    if m == 0:
        count = 0
        break
    p = m
if p <= E: count = 0
print(count)