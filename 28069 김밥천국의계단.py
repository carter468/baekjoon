# 김밥천국의 계단
# Gold 5, greedy

n,k = map(int,input().split())

while n > 1:
    if n%3 == 2: n -= 1
    else: n = n*2//3+n%3
    k -= 1

print('minigimbob' if k >= 1 else 'water')