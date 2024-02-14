# 생명 게임
# Gold 4, prefix sum, simulation

def count(x1,y1,x2,y2):
    x1,y1 = max(1,x1),max(1,y1)
    x2,y2 = min(n,x2),min(m,y2)
    return psum[x2][y2]-psum[x1-1][y2]-psum[x2][y1-1]+psum[x1-1][y1-1]

n,m,t = map(int,input().split())
k,a,b = map(int,input().split())
arr = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    s = input()
    for j in range(m):
        if s[j] == '.': arr[i][j+1] = 0
        else: arr[i][j+1] = 1

for _ in range(t):
    psum = [[0]*(m+1) for _ in range(n+1)]
    temp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            psum[i][j] = psum[i][j-1]+arr[i][j]
        for j in range(1,m+1):
            psum[i][j] += psum[i-1][j]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            c = count(i-k,j-k,i+k,j+k)
            if arr[i][j] == 1:
                if a <= c-1 <= b: temp[i][j] = 1
                else: temp[i][j] = 0
            else:
                if a < c <= b: temp[i][j] = 1
                else: temp[i][j] = 0
    arr = temp

for i in range(1,n+1):
    for j in range(1,m+1):
        print('*' if arr[i][j] else '.',end='')
    print()