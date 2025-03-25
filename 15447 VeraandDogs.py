# Vera and Dogs
# Gold 5, constructive, ad hoc

N,X = map(int,input().split())

if N <= X:
    print(-1)
else:
    p = [[] for _ in range(N)]
    for i in range(N):
        for j in range(X):
            p[i].append(i*X+j+1)
    
    s = [[] for _ in range(N)]
    idx = 0
    for i in range(N):
        for a in p[i]:
            while i == idx or len(s[idx]) == X: idx = (idx+1)%N
            s[idx].append(a)
            idx = (idx+1)%N
    
    for i in range(N):
        print(*p[i],*s[i])