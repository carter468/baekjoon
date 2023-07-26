# 제곱수 찾기
# Gold 5, bruteforce

n,m = map(int,input().split())
arr = [input() for _ in range(n)]

num = set()
for i in range(n):
    for j in range(m):
        num.add(int(arr[i][j]))
        for k in range(n):
            for l in range(-m+1,m):
                if (k,l) == (0,0): continue
                a,x,y = '',i,j
                while x < n and 0 <= y < m:
                    a += arr[x][y]
                    num.add(int(a))
                    num.add(int(a[::-1]))
                    x += k
                    y += l

sn = [-1]
for x in num:
    if x == int(x**0.5)**2:
        sn.append(x)

print(max(sn))