# Triangular Collection
# Gold 4, bruteforcing

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

result = 0
for i in range(n):
    for j in range(i+1,n):
        count = 0
        for k in range(j+1,n):
            if arr[i]+arr[j] > arr[k]: count += 1
        result += 2**count-1
print(result)