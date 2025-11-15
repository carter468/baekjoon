# 근수의 카드게임
# Gold 4, ad hoc, game theory

N,K = map(int,input().split())
print(-1 if K < N*2 else min(K-1,N*2))