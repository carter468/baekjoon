# 짝수번째 피보나치 수의 합
# Gold 2, 분할정복을 이용한 거듭제곱

def mat_m(a,b):
    c = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result = 0
            for k in range(2):
                result += a[i][k]*b[k][j] 
            c[i][j] = result % 1000000007
    return c

def mat_p(a,p): 
    if p<=1:
        return a
    if p%2==0:
        return mat_p(mat_m(a,a),p//2)
    else:
        return mat_m(a,mat_p(mat_m(a,a),p//2))

f = [[1,1],[1,0]]
n = int(input())
if n%2==0:
    print(mat_p(f,n)[0][0]-1)
else:
    print(mat_p(f,n-1)[0][0]-1)