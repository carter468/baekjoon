# 블랙 프라이데이
# Gold 5, bruteforcing

def solve():
    for i in range(N):
        if w[i] == C: return 1
        for j in range(i+1,N):
            k = C-w[i]-w[j]
            if k == 0 or k not in (w[i],w[j]) and k in s: return 1
    return 0

N,C = map(int,input().split())
w = tuple(map(int,input().split()))
s = set(w)

print(solve())