# 건너 아는 사이
# Gold 3, number theory

n = int(input())

seive = [True]*(n+1)
result = 0
for i in range(2,n+1):
    if seive[i]:
        result += i
        for j in range(i*i,n+1,i):
            if seive[j]:
                result += i
                seive[j] = False
print(result)