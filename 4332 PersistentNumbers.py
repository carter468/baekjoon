# Persistent Numbers
# Gold 5, greedy

import sys
input = sys.stdin.readline

while (n := int(input())) != -1:
    if n < 10:
        print(10+n)
        continue

    result = []
    while n >= 10:
        for i in range(9,1,-1):
            if n%i == 0:
                result.append(i)
                n //= i
                break
        else:
            print('There is no such number.')
            result = []
            break
    else:
        result.append(n)

    if result: print(''.join(map(str,sorted(result))))