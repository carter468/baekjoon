# 세기의 대결
# Gold 5, LIS, bruteforce

from bisect import bisect_left

def solve(arr):
    lis = [0]
    for x in arr:
        if lis[-1] < x:
            lis.append(x)
        else:
            lis[bisect_left(lis,x)] = x
    return len(lis)

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

yj = 0
for i in range(N):
    yj = max(yj,solve(A[i:]+A[:i]))
hg = 0
for i in range(N):
    hg = max(hg,solve(B[i:]+B[:i]))

if yj > hg: print('YJ Win!')
elif yj < hg: print('HG Win!')
else: print('Both Win!')