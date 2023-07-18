# 고층 건물
# Gold 4, geometry, bruteforce

n = int(input())
arr = tuple(map(int,input().split()))

result = [0]*n
for i in range(n-1):
    a = arr[i+1]-arr[i]
    result[i] += 1
    result[i+1] += 1
    for j in range(i+2,n):
        b = (arr[j]-arr[i])/(j-i)
        if b > a:
            a = b
            result[i] += 1
            result[j] += 1

print(max(result))