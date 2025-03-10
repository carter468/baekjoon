# Grudanje
# Gold 2, binary search, prefix sum

import sys
input = sys.stdin.readline

def check(x):
    st = list(s)
    for i in range(x):
        st[p[i]-1] = ''

    count = [[0]*(N+1) for _ in range(26)]
    for i in range(N):
        if st[i]: count[ord(st[i])-97][i] = 1
        for j in range(26):
            count[j][i] += count[j][i-1]
    
    for a,b in arr:
        for i in range(26):
            if count[i][b-1]-count[i][a-2] > 1: return False
    return True

s = input().strip()
N = len(s)
arr = [tuple(map(int,input().split())) for _ in range(int(input()))]
p = tuple(map(int,input().split()))

lo,hi = -1,N
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)