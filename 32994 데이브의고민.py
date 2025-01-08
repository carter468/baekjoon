# 데이브의 고민
# Gold 4, ad hoc, constructive

N,M = map(int,input().split())

arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = (i*2+j)%5+1

for a in arr:
    print(*a)