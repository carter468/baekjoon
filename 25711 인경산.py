# 인경산
# Gold 5, prefix sum

import sys
input = sys.stdin.readline

def solve(X,Y):
    arr = [0]
    for i in range(N-1):
        x1,y1 = X[i],Y[i]
        x2,y2 = X[i+1],Y[i+1]
        d = ((x1-x2)**2+(y1-y2)**2)**0.5
        if y1 > y2:
            arr.append(arr[-1]+d)
        elif y1 == y2:
            arr.append(arr[-1]+d*2)
        else:
            arr.append(arr[-1]+d*3)
    return arr

N,Q = map(int,input().split())
X = tuple(map(int,input().split()))
Y = tuple(map(int,input().split()))

dist = solve(X,Y)
dist_r = solve(X[::-1],Y[::-1])

for _ in range(Q):
    i,j = map(int,input().split())
    if i < j: 
        print(dist[j-1]-dist[i-1])
    else: 
        print(dist_r[N-j]-dist_r[N-i])