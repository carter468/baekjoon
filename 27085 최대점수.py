# 최대 점수
# Gold 2, greedy, two pointer

N,S = map(int,input().split())
A = tuple(map(int,input().split()))

t = 0
l = r = S-1
while True:
    f = False
    nt = t
    for i in range(l-1,-1,-1):
        nt += A[i]
        if nt < 0: break
        if nt >= t and i != l:
            l = i
            t = nt
            f = True
    nt = t
    for i in range(r+1,N):
        nt += A[i]
        if nt < 0: break
        if nt >= t and i != r:
            r = i
            t = nt
            f = True

    if not f: break
print(t)