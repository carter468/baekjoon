# 정수를 끝까지 외치자
# Gold 5, game theory

n,k = map(int,input().split())
ban = [0]*(n+1)
for a in map(int,input().split()):
    ban[a] = 1

while n > 0:
    while ban[n] == 1:
        n -= 1
    if 1 <= n <= k:
        print(1)
        break
    n -= k+1
else: print(0)