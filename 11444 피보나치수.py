# 피보나치 수 6

def M(A,B): #A*B
    tmp = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result = 0
            for k in range(2):
                result += A[i][k]*B[k][j] 
            tmp[i][j] = result % 1000000007
    return tmp

def S(A,n): #A^n
    if n == 1:
        return A
    tmp = S(A,n//2)
    if n % 2 == 0:
        return M(tmp,tmp)
    else:
        return M(M(tmp,tmp),A)

F = [[1,1],[1,0]]
n = int(input())

if n == 1:
    print(1)
else:
    ans = S(F,n-1)
    print(ans[0][0])