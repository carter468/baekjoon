# Card Game
# Gold 1, math, combinatorics

from collections import defaultdict

N,C = map(int,input().split())
A = tuple(map(int,input().split()))

count = defaultdict(int)
count1 = defaultdict(int)
for i in range(N):
    count1[A[i]] += 1
    for j in range(i+1,N):
        count[A[i]+A[j]] += 1

result = 0
for i in range(N):
    for j in range(i+1,N):
        a,b = A[i],A[j]
        if C == 0:
            if a == b:
                x = count1[a]
                result += count[a+b]-(x*(x-1)//2-(x-2)*(x-3)//2)
            else:
                x,y = count1[a],count1[b]
                result += count[a+b]-x*y+(x-1)*(y-1)
        else:
            x = a+b-C
            t = count[x]
            for y in (a,b):
                t -= count1[x-y]
                if x-y == y: t += 1
            result += t
print(result)