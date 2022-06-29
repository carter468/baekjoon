# 행렬 곱셈
import sys
input = sys.stdin.readline

def cal(x,y):
    global m
    ans = 0
    for i in range(m):
        ans += a[x][i]*b[i][y]
    return ans

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
m,k = map(int,input().split())
b = []
for _ in range(m):
    b.append(list(map(int,input().split())))

# n,m = 2,2
# a = [[1,2],[3,4]]
# m,k = 2,4
# b = [[-1,-2,0,1],[0,0,3,4]]


ans = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        ans[i][j] = cal(i,j)

for i in range(n):
    print(' '.join(map(str,ans[i])))