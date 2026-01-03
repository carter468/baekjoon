# generator
# Gold 5, constructive, implementation, bruteforcing

N = int(input())
L = list(map(int,input().split()))
S = input()

if S == 'no':
    s = set(range(1,2001))
    for l in L:
        s.discard(l)
    for i in range(N):
        if L[i] == 0:
            L[i] = s.pop()
    print(*L)
else:
    for i in range(1,N//2+1):
        t = list(L)
        a = L[:i]
        b = L[-i:]
        for j in range(i):
            k = -i+j
            if t[j] == 0 and t[k] == 0:
                t[j],t[k] = 1,1
            elif t[j] == 0:
                t[j] = t[k]
            elif t[k] == 0:
                t[k] = t[j]
            elif t[j] != t[k]:
                break
        else:
            for i in range(N):
                if t[i] == 0:
                    t[i] = 1
            exit(print(*t))