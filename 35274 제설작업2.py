# 제설 작업 2
# Gold 2, greedy, binary search, simulation

def check(x):
    arr = [A[i][:] for i in range(N)]
    t = 0
    idx = 0
    while idx < N:
        a,i = arr[idx]
        b = (a-1)//x+1
        t += b
        c = b*x-a
        idx += 1
        while idx < N and c and arr[idx][1] < i+L:
            aa,_ = arr[idx]
            if c > aa:
                c -= aa
                idx += 1
            else:
                arr[idx][0] -= c
                if arr[idx][0] == 0: idx += 1
                break
    return t <= M

N,M,L = map(int,input().split())
A = []
for i,a in enumerate(map(int,input().split())):
    if a: A.append([a,i])
N = len(A)

lo,hi = 0,10**16
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi if hi < 10**16 else -1)