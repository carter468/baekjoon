# 카르텔 님 게임
# Platinum 5, game theory

n,k = map(int,input().split())

if k+3 <= n <= k*2+1 or n == k: print('A and B win')
else: print('C win')