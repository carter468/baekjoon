# 그리고 하나가 남았다
# Platinum 5, DP

while True:
    N,K,M = map(int,input().split())
    if N == 0: break

    x = 0
    for i in range(1,N):
        x = (x+K)%i

    x = (x+M+1)%N
    if x == 0: x = N
    print(x)