# 바둑돌게임

n = int(input())
total = 0
for i in range(1,450):
    total += i
    if total >= n:
        break
if i%2==0:
    if total == n:
        print(i+1)
    else:
        print(0)
else:
    print(total-n)