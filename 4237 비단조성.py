# 비 단조성
# Gold 4, greedy, ad hoc

for _ in range(int(input())):
    N,*A = map(int,input().split())

    k = 0
    count = 1
    for i in range(N-1):
        if k == 0 and A[i] > A[i+1]:
            k = 1
            count += 1
        elif k == 1 and A[i] < A[i+1]:
            k = 0
            count += 1
    print(count)