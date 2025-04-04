# Min Max Mex
# Gold 4, greedy

N,K = map(int,input().split())
A = sorted(map(int,input().split()))

if A[0] > 0: print(0)
else:
    mex = 0
    c = 0
    for i in range(N):
        if A[i] == mex: c += 1
        else:
            if c <= K:
                print(mex)
                break
            mex += 1
            c = 1
            if A[i] > mex:
                print(mex)
                break
    else:
        if c > K: mex += 1
        print(mex)

mex = 0
for i in range(N):
    if mex <= A[i]:
        if A[i]-mex > K:
            print(mex+K)
            break
        K -= A[i]-mex
        mex = A[i]+1
else: print(mex+K)