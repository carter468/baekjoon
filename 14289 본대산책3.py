# 본대 산책 3
# Gold 1, exponentiation by squaring

MOD = 10**9+7

def pow(mat,p):
    def mul(x,y):
        result = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                c = 0
                for k in range(N):
                    c += x[i][k]*y[k][j]
                result[i][j] = c%MOD
        return result
    
    if p == 1: return mat
    temp = pow(mul(mat,mat),p//2)
    if p%2 == 0: return temp
    else: return mul(temp,mat)

N,M = map(int,input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    arr[a][b] = 1
    arr[b][a] = 1

print(pow(arr,int(input()))[0][0])