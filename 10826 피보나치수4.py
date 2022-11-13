# 피보나치 수 4
# Silver 5

n = int(input())
fibo = [0]*10001
fibo[1] = 1
for i in range(2,n+1):
    fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo[n])