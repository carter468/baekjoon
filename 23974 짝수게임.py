# 짝수 게임
# Gold 3, game theory

n,k = map(int,input().split())

if (n == 0 and k%6 == 1) or (n == 1 and k%6 in (0,5)): print('HS')
else: print('YG')
