# 인버전 과제
# Gold 3, ad hoc

import sys
input = sys.stdin.readline
N,I = map(int,input().split())

f = True
for i in range(1,N+1):
    if f == False:
        print(i-1,i)
    else:
        print(i,i)
    sys.stdout.flush()
    x = int(input())
    if x == 0: break
    if x < I: 
        f = True
        I = x
    else:
        f = False