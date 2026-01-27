# Stadium
# Gold 5, prefix sum

for _ in range(int(input())):
    N = int(input())
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))

    t = sum(B)
    c = 0
    for i in range(N):
        c += B[i]
        if c*2 >= t: break
    print(A[i])