# 닭강정의 전설
# Gold 5, prefix sum

import sys
input = sys.stdin.readline

def psum(a,b,c,d):
    return ps[c][d]-ps[a-1][d]-ps[c][b-1]+ps[a-1][b-1]

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

ps = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        ps[i][j] = ps[i-1][j]+ps[i][j-1]-ps[i-1][j-1]+arr[i-1][j-1]

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    x = psum(a+1,b+1,c-1,d-1)
    x -= psum(a,b,a,d)
    x -= psum(c,b,c,d)
    x -= psum(a+1,b,c-1,b)
    x -= psum(a+1,d,c-1,d)
    print(x)