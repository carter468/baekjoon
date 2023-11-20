# 별 안에 별 안에 별 찍기
# Gold 5, recursion

n = int(input())
arr = ((0,0,1,0,0),(0,0,1,0,0),(1,1,1,1,1),(0,1,1,1,0),(0,1,0,1,0))

result = [[' ']*(5**n) for _ in range(5**n)]

def star(p,x,y):
    if p == 0:
        result[x][y] = '*'
        return
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                star(p-1,5**p*i+x,5**p*j+y)

if n == 0:
    print('*')
    exit()
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            star(n-1,i,j)
for r in result:
    print(''.join(r))