# 행렬 제곱

def m(A,B): # A*B
    n = len(A)
    result_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result = 0
            for k in range(n):
                result += A[i][k]*B[k][j]
            result_mat[i][j] = result % 1000
    return result_mat

def squ(A,b):   # A^b
    if b==1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    tmp = squ(A,b//2)
    if b%2 == 0:
        return m(tmp,tmp)
    else:
        return m(m(tmp,tmp),A)
        
# n,b=2,5
# a = [[1,2],[3,4]]
n,b = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

ans = squ(a,b)

for x in ans:
    print(*x)