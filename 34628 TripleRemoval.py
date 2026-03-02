# Triple Removal
# Gold 2, prefix sum

import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    N,Q = map(int,input().split())
    A = tuple(map(int,input().split()))

    sa = [0]*(N+1)
    sb = [0]*(N+1)
    sc = [0]*(N+1)
    for i in range(1,N+1):
        sa[i] += sa[i-1]
        sb[i] += sb[i-1]
        sc[i] += sc[i-1]
        if A[i-1] == 0: sa[i] += 1
        else: sb[i] += 1
        if i > 1 and A[i-1] == A[i-2]: sc[i] += 1

    for _ in range(Q):
        l,r = map(int,input().split())
        a = sa[r]-sa[l-1]
        b = sb[r]-sb[l-1]
        if a%3 == 0 and b%3 == 0:
            result.append((a+b)//3+(1 if sc[r] == sc[l] else 0))
        else:
            result.append(-1)
print(*result,sep='\n')