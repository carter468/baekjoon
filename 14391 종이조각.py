# 종이 조각
# Gold 3, bruteforce, bitmask

n,m = map(int,input().split())
arr = [tuple(map(int,input())) for _ in range(n)]

result = 0
for i in range(1<<n*m):
    total = 0
    for row in range(n):
        t = 0
        for col in range(m):
            idx = row*m+col
            if i&(1<<idx) != 0:
                t = t*10+arr[row][col]
            else:
                total += t
                t = 0
        total += t
    for col in range(m):
        t = 0
        for row in range(n):
            idx = row*m+col
            if i&(1<<idx) == 0:
                t = t*10+arr[row][col]
            else:
                total += t
                t = 0
        total += t
    result = max(result,total)
print(result)