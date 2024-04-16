# Professor KCM
# Gold 4, math

from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    result = defaultdict(int)
    for a in map(int,input().split()):
        count = defaultdict(int)
        for i in range(2,int(a**0.5)+1):
            while a%i == 0:
                count[i] += 1
                a //= i
        if a > 1: count[a] += 1
        for c in count:
            result[c] = max(result[c],count[c])

    answer = 1
    for c in result:
        answer = (answer*(c**result[c]))%(10**9+7)
    print(answer)