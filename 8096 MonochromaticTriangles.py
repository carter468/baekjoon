# Monochromatic Triangles
# Platinum 4, combinatorics

import sys
input = sys.stdin.readline

n,m = int(input()),int(input())
arr = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    arr[a] += 1
    arr[b] += 1

result = 0
for a in arr:
    result += a*a
print(n*(n-1)*(n-2)//6-(n-1)*m+result//2)