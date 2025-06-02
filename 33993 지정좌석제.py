# 지정좌석제
# Gold 5, prefix sum

import sys
input = sys.stdin.readline

N,R,C,W = map(int,input().split())
arr = [[0]*(C+1) for _ in range(R+1)]
for _ in range(N):
    x,y = map(int,input().split())
    arr[x][y] = 1

psum = [[0]*(C+1) for _ in range(R+1)]
for i in range(1,R+1):
    for j in range(1,C+1):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+arr[i][j]

W //= 2
result = [0,0,0]
for i in range(1,R+1):
    for j in range(1,C+1):
        if arr[i][j] == 0:
            a,b,c,d = max(1,i-W),max(1,j-W),min(R,i+W),min(C,j+W)
            count = psum[c][d]-psum[c][b-1]-psum[a-1][d]+psum[a-1][b-1]
            if count > result[0]: result = [count,i,j]

print(result[0])
print(*result[1:])