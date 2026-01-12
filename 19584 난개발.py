# 난개발
# Gold 3, coordinate compression, prefix sum

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [int(input().split()[1]) for _ in range(N)]

s = sorted(set(arr))
l = len(s)
dic = {y:i for i,y in enumerate(s)}

count = [0]*(l+2)
for _ in range(M):
    u,v,c = map(int,input().split())
    a,b = dic[arr[u-1]],dic[arr[v-1]]
    if a > b: a,b = b,a
    count[a] += c
    count[b+1] -= c

result = 0
for i in range(l):
    count[i] += count[i-1]
    result = max(result,count[i])
print(result)