# 간판 만들기
# Gold 5, DP

INF = 10**10

input()
S = input()
A = tuple(map(int,input().split()))

u = o = s = p = c = INF
for i,ch in enumerate(S):
    a = A[i]
    if ch == 'U':
        u = min(u,a)
    elif ch == 'O':
        o = min(o,u+a)
    elif ch == 'S':
        s = min(s,o+a)
    elif ch == 'P':
        p = min(p,s+a)
    elif ch == 'C':
        c = min(c,p+a)

print(c if c < INF else -1)