# 마슈 반데드와 마법사의 격자판
# Gold 3, constructive, ad hoc

N,K = map(int,input().split())

if N*N//2 > K or (N%2 == 0 and K%2 == 1): print(-1)
else:
    k = K
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i+j-K)%2 == 1:
                arr[i][j] += 1
                k -= 1

    x,k = divmod(k,N*N*2)
    for i in range(N):
        for j in range(N):
            arr[i][j] += x*2
    
    for i in range(N):
        if k == 0: break
        for j in range(N):
            if k == 0: break
            if (i+j+K)%2 == 0:
                arr[i][j] += 2
                k -= 2
    for i in range(N):
        if k == 0: break
        for j in range(N):
            if k == 0: break
            if (i+j+K)%2 == 1:
                arr[i][j] += 2
                k -= 2
    
    for a in arr:
        print(*a)