# 좋은 수
# Gold 3, DP

n = int(input())
arr = tuple(map(int,input().split()))

result = 0
c = [0]*400001
for i in range(n):
    for j in range(i):
        if c[arr[i]-arr[j]]:
            result += 1
            break
    for j in range(i+1):
        c[arr[i]+arr[j]] = 1
print(result)