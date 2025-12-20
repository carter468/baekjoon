# Triangles
# Gold 2, greedy, bruteforcing

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]

    result = [0]*10
    t1 = [[] for _ in range(10)]
    t2 = [[] for _ in range(10)]
    for i in range(N):
        x = [[-1]*2 for _ in range(10)]
        for j in range(N):
            k = int(arr[i][j])
            if x[k][0] == -1:
                x[k][0] = j
            x[k][1] = j
        for n in range(10):
            a,b = x[n]
            result[n] = max(result[n],(b-a)*max(i,N-i-1))
            if a != -1:
                t1[n].append((i,a))
                t2[n].append((i,b))
        y = [[-1]*2 for _ in range(10)]
        for j in range(N):
            k = int(arr[j][i])
            if y[k][0] == -1:
                y[k][0] = j
            y[k][1] = j
        for n in range(10):
            a,b = y[n]
            result[n] = max(result[n],(b-a)*max(i,N-i-1))
    
    for n in range(10):
        for a,b in t1[n]:
            for c,d in t2[n]:
                result[n] = max(result[n],abs(a-c)*max(b,N-b-1,d,N-d-1),abs(b-d)*max(a,N-a-1,c,N-c-1))
    
    print(*result)