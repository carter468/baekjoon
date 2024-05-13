# RUN Number
# Gold 5, greedy

for _ in range(int(input())):
    n,k = map(int,input().split())
    result = []
    while k:
        a = int(str(k)[0])
        while int('1'*n)*a > k:
            a -= 1
            if a == 0:
                a = 9
                n -= 1
        b = int('1'*n)*a
        result.append(b)
        k -= b
    print(len(result))
    print(*result)