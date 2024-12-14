# 백신 개발
# Gold 5, bruteforcing

import itertools

def solve(p):
    k = len(V[p[0]])
    now = V[p[0]]
    for i in range(N-1):
        nxt = V[p[i+1]]
        for j in range(min(len(now),len(nxt)),0,-1):
            if now[-j:] == nxt[:j]: 
                k += len(nxt)-j
                now += nxt[j:]
                break
        else:
            return 99
    return k

N = int(input())
V = [input() for _ in range(N)]

result = 99
for p in itertools.permutations(range(N)):
    result = min(result,solve(p))
print(result)