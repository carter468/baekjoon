# 센서
# Gold 5, greedy

n,k = int(input()),int(input())
arr = sorted((map(int,input().split())))

dist = []
for i in range(n-1):
    dist.append(arr[i+1]-arr[i])
print(sum(sorted(dist)[:n-k]))
