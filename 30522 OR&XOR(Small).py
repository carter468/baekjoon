# OR & XOR (Small)
# Gold 2, greedy, bruteforcing, bitmask

from collections import defaultdict

N,p = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

result = 0
countA = defaultdict(int)
countB = defaultdict(int)
for i in range(N):
    countA[A[i]] += 1
    countB[B[i]] += 1
    result += A[i]+B[i]
result *= N

count = [0]*(1<<10)
for i in range(1<<10):
    for j in range(1<<10):
        count[i&j] += countA[i]*countB[j]

for i in range(1<<10):
    result -= i*count[i]*2

for i in range((1<<10)-1,-1,-1):
    if count[i] >= p:
        result += i*p
        break
    result += i*count[i]
    p -= count[i]
print(result)