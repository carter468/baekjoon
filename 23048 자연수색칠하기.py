# 자연수 색칠하기
# Gold 5, 에라토스테네스의 체

N = int(input())

seive = [0]*(N+1)
seive[1] = 1
n = 1
for i in range(2,N+1):
    if seive[i]==0:
        n += 1
        for j in range(i,N+1,i):
            seive[j] = n

print(n)
print(*seive[1:])