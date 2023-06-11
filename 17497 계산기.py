# 계산기
# Gold 3, 수학

n = int(input())

result = []
while n:
    if n&1:
        result.append('[/]')
        n *= 2
    elif n&2:
        result.append('[+]')
        n -= 2
    else:
        result.append('[*]')
        n //= 2

print(len(result))
print(*result[::-1])