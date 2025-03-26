# 생일 멘션이 너무 많아
# Gold 5, prefix sum

N,M = map(int,input().split())
P = tuple(map(int,input().split()))

t = 0
c = 0
for p in P:
    if p >= 2:
        c += 1
        t += p
if c == 0: m = 0
else: m = t//c

result = [0]*(M+1)
for p in P:
    if p <= m:
        if p > M:
            exit(print(-1))
        result[0] += 1
        result[p] -= 1
    else:
        result[0] += 1
        result[1] -= 1

for i in range(M):
    result[i+1] += result[i]
print(*result[:M])