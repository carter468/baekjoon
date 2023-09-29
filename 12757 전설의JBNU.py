# 전설의 JBNU
# Gold 3, binary_serach, hash_set

import sys
input = sys.stdin.readline

def bs(t):
    lo,hi = -1,len(key)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if key[mid] < t: lo = mid
        else: hi = mid
    return hi

def findkey(x):
    if x in db: return x
    idx = bs(a[1])
    if idx == 0:
        if abs(key[idx]-x) <= k: return key[idx]
    elif idx == len(key):
        if abs(key[idx-1]-x) <= k: return key[idx-1]
    else:
        l = x-key[idx-1]
        r = key[idx]-x
        if l == r and l <= k: return -2
        if l < r and l <= k: return key[idx-1]
        if l > r and r <= k: return key[idx]
    return -1

n,m,k = map(int,input().split())

db = {}
key = []
for _ in range(n):
    a,b = map(int,input().split())
    db[a] = b
    key.append(a)
key.sort()

for _ in range(m):
    a = tuple(map(int,input().split()))
    if a[0] == 1:
        db[a[1]] = a[2]
        key.insert(bs(a[1]),a[1])
    else:
        i = findkey(a[1])
        if a[0] == 2:
            if i >= 0:
                db[i] = a[2]
        else:
            if i >= 0: print(db[i])
            elif i == -1: print(i)
            else: print('?')