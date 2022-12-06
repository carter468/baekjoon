# 거듭제곱
# Silver 4, 비트마스킹, 수학

n = int(input())
i = 0
answer = 0
while n:
    answer += (3**i)*(n%2)
    i += 1
    n //= 2
print(answer)