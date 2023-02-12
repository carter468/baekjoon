# 피보나치 수의 합
# Gold 1, 분할정복을 이용한 거듭제곱

# 행렬

def matrix_mul(m1,m2): 
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            entry = 0
            for k in range(2):
                entry += m1[i][k]*m2[k][j] 
            result[i][j] = entry%MOD
    return result

def matrix_pow(m,n): 
    if n==0 or n==1:
        return m
    if n%2==0:
        return matrix_pow(matrix_mul(m,m),n//2)
    else:
        return matrix_mul(matrix_pow(m,n-1),m)

def fib(n):
    return matrix_pow(M,n-1)[0][0]

MOD = 10**9
M = (1,1),(1,0)

a,b = map(int,input().split())
print((fib(b+2)-fib(a+1))%MOD)

########################################
# 도가뉴 항등식

def fib(n):
    if n in f:
        return f[n]
    if n%2==0:
        k = n//2
        f[n] = (2*fib(k-1)+fib(k))*fib(k)%MOD
        return f[n]
    else:
        k = n//2
        f[n] = (fib(k+1)**2+fib(k)**2)%MOD
        return f[n]
    
MOD = 10**9
f = {0:0,1:1}

a,b = map(int,input().split())
print((fib(b+2)-fib(a+1))%MOD)