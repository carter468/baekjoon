# 경인 국가의 행사
# Gold 1, greedy, ad hoc, case work

import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    N = int(input())
    A = []
    for i,n in enumerate(map(int,input().split())):
        A.append((n,i))
    A.sort()

    x,y = [0]*N,[0]*N
    c = N//2+1
    for n,i in A[:c]:
        a = n//2+1
        x[i] = n-a
        y[i] = a
    for n,i in A[c:]:
        x[i] = n
        y[i] = 0

    if sum(x) > sum(y):
        print('YES')
        print(*x)
        print(*y)
        continue

    x,y = [0]*N,[0]*N
    if N%2 == 0:
        t = -1
        for n,i in A:
            if n%2 == 0:
                t = i
                x[i] = n//2
                y[i] = n//2
                break
            
        if t != -1:
            c = 0
            for n,i in A:
                if i == t: continue
                if N//2 > c:
                    a = n//2+1
                    x[i] = n-a
                    y[i] = a
                    c += 1
                else:
                    x[i] = n
                    y[i] = 0
            
    if sum(x) > sum(y):
        print('YES')
        print(*x)
        print(*y)
    else:
        print('NO')