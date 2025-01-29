# TAIDADA
# Gold 4, ad hoc, constructive

N,M,K = map(int,input().split())

result = []
s = set(range(1,min(400000,M)+1))
for _ in range(N):
    if not s: exit(print(-1))
    x = s.pop()
    result.append(x)
    y = x^K
    if y in s: s.remove(y)
print(*result)