# Rise and Fall
# Gold 5, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = input().strip()

    l = len(N)
    result = ''
    p = '0'
    for i in range(l):
        if N[i] >= p:
            result += N[i]
            p = N[i]
        else:
            break
    else:
        print(result)
        continue
    p = '9'
    for j in range(i,l):
        if N[j] <= p:
            result += N[j]
            p = N[j]
        else:
            result += p*(l-j)
            break
    print(result)