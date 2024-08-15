# 소수 수열
# Gold 5, number theory, constructive

M = 1000001
seive = [True]*M
for i in range(2,int(M**0.5)+1):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False

n,k = map(int,input().split())

result = []
for i in range(2,M):
    if seive[i] and i%k == 1: result.append(i)
print(*result[:n])
