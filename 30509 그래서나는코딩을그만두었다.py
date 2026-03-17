# 그래서 나는 코딩을 그만두었다
# Platinum 3, greedy, binary search

import sys
input = sys.stdin.readline

def check(x):
    s,m = S,M+(N-x)*R
    for i in range(x):
        u,v = A[i]
        if s+m > u+v:
            m += max(0,u-s)
        elif s+m < u+v:
            break
    else:
        return True
    
    B = sorted(A[i:],reverse=True)
    for j in range(x-i):
        m -= L+max(0,s-B[j][0])
        if m <= 0: return False
    return True

N,L,R = map(int,input().split())
S,M = map(int,input().split())
A = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:(x[0]+x[1],-x[0]))

yes,no = 0,N+1
while yes+1 < no:
    mid = (yes+no)//2
    if check(mid): yes = mid
    else: no = mid
print(yes)