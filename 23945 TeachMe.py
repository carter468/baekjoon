# Teach Me
# Gold 2, hash set

from collections import defaultdict
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    N,S = map(int,input().split())
    count = defaultdict(int)
    for _ in range(N):
        _,*skill = map(int,input().split())
        count[tuple(sorted(skill))] += 1

    result = N*N
    for x in count:
        a = count[x]
        c = len(x)
        for i in range(1<<c):
            subset = []
            for j in range(c):
                if i>>j&1:
                    subset.append(x[j])
            subset = tuple(subset)
            if subset in count:
                b = count[subset]
                result -= a*b

    print(f'Case #{tc+1}: {result}')