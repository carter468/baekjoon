# 방법을 출력하지 않는 숫자 맞추기

n = int(input())
x = input()
y = input()
dp = [[[0,0],[0,0]] for _ in range(n)]
a,b = int(x[0]),int(y[0])
dp[0][0] = [(10+b-a)%10,(10+b-a)%10]
dp[0][1] = [(10+a-b)%10,0]
for i in range(1,n):
    a,b = int(x[i]),int(y[i])
    