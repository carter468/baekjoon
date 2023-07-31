# 오민식
# Gold 4, math, seive

n = int(input())

result = 1
p = [1]*(n+1)
for i in range(2,n+1):
    if p[i]:
        for j in range(i,n+1,i):
            p[j] = 0
        k = i
        while k*i <= n:
            k *= i
        result = result*k%987654321

print(result)