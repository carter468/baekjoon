# 행렬 덧셈

n,m = map(int,input().split())
matrix_sum = []
for _ in range(n):
    matrix_sum.append(list(map(int,input().split())))
for i in range(n):
    row_b = list(map(int,input().split()))
    for j in range(m):
        matrix_sum[i][j] += row_b[j]
for x in matrix_sum:
    print(*x)