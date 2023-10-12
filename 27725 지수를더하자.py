# 지수를 더하자
# Gold 4, number theory

n = int(input())
p = tuple(map(int,input().split()))
k = int(input())

result = 0
for x in p:
    a = x
    while a <= k:
        result += k//a
        a *= x
print(result)