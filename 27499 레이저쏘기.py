# 레이저 쏘기
# Gold 2, hash set, geometry

from collections import defaultdict
import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N,M,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

ext = []
for x,y in arr:
    x1 = M-x
    for i in range(K):
        ext.append(((x,x1)[i%2]+M*i,y))

count = defaultdict(int)
for x,y in ext:
    g = gcd(x,y)
    count[(x//g,y//g)] += 1

result = 0
for a in count:
    result = max(result,count[a])
print(result)