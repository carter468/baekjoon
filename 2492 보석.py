# 보석
# Gold 3, bruteforcing

n,m,t,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(t)]

result = [-1]
for x in range(t):
    a = arr[x][0]
    for y in range(t):
        b = arr[y][1]
        if a+k > n: a = n-k
        if b-k < 0: b = k
        count = 0
        for i in range(t):
            if a <= arr[i][0] <= a+k and b-k <= arr[i][1] <= b:
                count += 1
        if count > result[0]: result = [count,(a,b)]
        
print(*result[1])
print(result[0])
