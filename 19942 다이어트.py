# 다이어트
# Gold 4, bruteforcing
 
n = int(input())
m = tuple(map(int,input().split()))
arr = [tuple(map(int,input().split())) for _ in range(n)]

result = [9999,0]
for i in range(1<<n):
    temp = [0]*5
    for j in range(n):
        if i>>j&1:
            for k in range(5):
                temp[k] += arr[j][k]
    if temp[0] >= m[0] and temp[1] >= m[1] and temp[2] >= m[2] and temp[3] >= m[3]:
        x = []
        for j in range(n):
            if i>>j&1:
                x.append(j+1)
        if temp[4] < result[0]: result = [temp[4],x]
        elif temp[4] == result[0] and x < result[1]: result[1] = x

if result[0] == 9999: print(-1)
else:
    print(result[0])
    print(*result[1])
