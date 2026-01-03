# 룩 vs 폰
# Platinum 5, ad hoc

N,M,K = map(int,input().split())

if N >= M: print(1)
elif N == 1: print(2)
elif N == 2:
    if K > 3: print(3)
    else: print(4)
else: print(5)