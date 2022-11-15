# 알고리즘 수업 - 피보나치수열 2
# Silver 4, 분할정복

n = int(input())
M = 1000000007

def matrix_multiple(a, b):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (a[i][k] * b[k][j])%M
    return temp

def matrix_pow(n, result):
    if n == 1:
        return result
    if n % 2 == 0:
        temp = matrix_pow(n//2, result)
        return matrix_multiple(temp, temp)
    else:
        temp = matrix_pow(n-1, result)
        return matrix_multiple(temp, result)

a = [[1, 1], [1, 0]]
print(matrix_pow(n-1, a)[0][0]%M,n-2)

# pypy, 다이나믹 프로그래밍

n = int(input())
M = 1000000007

a,b = 1,1
for i in range(n-2):
    a,b = (a+b)%M,a
print(a,n-2)