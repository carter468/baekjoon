# 암호 찾기
# Platinum 5, hashing

def solve(S):
    h1,h2,x1,x2 = 0,0,1,1
    for i in range(K):
        h1 = (h1*P1+S[i])%M1
        h2 = (h2*P2+S[i])%M2
        if i > 0:
            x1 = x1*P1%M1
            x2 = x2*P2%M2
    result = {h1*M2+h2}
    for i in range(K,N):
        h1 = ((h1-S[i-K]*x1)%M1*P1+S[i])%M1
        h2 = ((h2-S[i-K]*x2)%M2*P2+S[i])%M2
        result.add(h1*M2+h2)
    return result

N,K = map(int,input().split())
A = list(map(int,input()))
B = list(map(int,input()))

M1,M2,P1,P2 = 10**9+7,10**9+9,29,37

print(len(solve(A)&solve(B)))