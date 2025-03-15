# AND
# Gold 2, ad hoc, constructive

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = tuple(map(int,input().split()))

    x = m = arr[0]
    for a in arr:
        x &= a
        m = min(m,a)
        
    if x < m:
        print(-1)
    else:
        print(N*2)
        for a in arr:
            print(a,x,end=' ')
        print()