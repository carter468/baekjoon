# 수문
# Gold 5, bruteforcing, bitmasking

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

table = []
for i in range(1<<n):
    a,b = 0,0
    for j in range(n):
        if i>>j&1:
            a += arr[j][0]
            b += arr[j][1]
    table.append((a,b))

for i in range(int(input())):
    v,t = map(int,input().split())
    result = 10**10
    for a,b in table:
        if a*t >= v: result = min(result,b)
    if result == 10**10: result = 'IMPOSSIBLE'
    print(f'Case {i+1}: {result}')