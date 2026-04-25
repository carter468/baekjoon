# 부분 직사각형
# Gold 5, combinatorics

N,M = map(int,input().split())
table = [input()*2 for _ in range(N)]

table += table
N,M = N*2,M*2
result = [0]*26
for i in range(N):
    for j in range(M):
        result[ord(table[i][j])-65] += (i+1)*(j+1)*(N-i)*(M-j)
print(*result,sep='\n')