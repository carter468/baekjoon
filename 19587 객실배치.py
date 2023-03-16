# 객실배치
# Gold 1, DP, 거듭제곱 분할정복

def m_mul(a,b):
    c = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t = 0
            for k in range(3):
                t += a[i][k]*b[k][j]
            c[i][j] = t%MOD
    return c

def m_pow(a,n):
    if n==0: return [[1,1,1]]
    if n==1: return a
    if n%2: return m_mul((m_pow(a,n-1)),a)
    return m_pow(m_mul(a,a),n//2)

MOD = 10**9+7
answer = 0
for x in m_pow([[1,1,1],[1,0,1],[1,1,0]],int(input())-1):
    answer += sum(x)
print(answer%MOD)