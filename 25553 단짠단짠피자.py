# 단짠단짠 피자
# Gold 1, sliding window

import sys
input = sys.stdin.readline

N,Q,K = map(int,input().split())
A = tuple(map(int,input().split()))

odd,even = (K+1)//2,K//2
t = sum(A[:K])
dic = {(odd,even):(1,t)}
for i in range(1,N):
    j = (i+K-1)%N
    if i%2 == 0: even -= 1
    else: odd -= 1
    if j%2 == 0: odd += 1
    else: even += 1
    t += A[j]-A[i-1]
    if (odd,even) not in dic or t > dic[((odd,even))][1]: dic[(odd,even)] = (i+1,t)

x,y = 0,0
for _ in range(Q):
    q = tuple(map(int,input().split()))
    if q[0] == 1: x += q[1]
    elif q[0] == 2: y += q[1]
    else:
        arr = []
        for key in dic:
            o,e = key
            i,t = dic[key]
            arr.append((i,t+o*x+e*y))
        print(*sorted(arr,key=lambda x:(-x[1],x[0]))[0])