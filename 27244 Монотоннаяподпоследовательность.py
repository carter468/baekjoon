# Монотонная подпоследовательность
# Platinum 5, ad hoc, constructive

N,K = map(int,input().split())

if N > K*K:
    print(-1)
else:
    result = []
    i = K
    while i-K <= N:
        result += range(min(N,i),i-K,-1)
        i += K
    print(*result)