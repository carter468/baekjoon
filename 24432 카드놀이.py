# 카드 놀이
# Gold 4, bruteforcing, binary search

import itertools,bisect

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    bob = tuple(map(int,input().split()))
    alice = tuple(map(int,input().split()))

    arr1 = set()
    for p in itertools.combinations(range(n),k):
        a = 0
        for i in p:
            a += bob[i]
        arr1.add(a)
    
    arr2 = set()
    for p in itertools.combinations(range(m),k):
        a = 0
        for i in p:
            a += alice[i]
        arr2.add(a)
    
    arr2 = sorted(arr2)
    l2 = len(arr2)
    minscore = 10**9
    for a in arr1:
        i = bisect.bisect_left(arr2,a)
        for j in (i-1,i,i+1):
            if 0 <= j < l2:
                minscore = min(minscore,abs(a-arr2[j]))
    print(minscore,max(max(arr1)-arr2[0],arr2[-1]-min(arr1)))