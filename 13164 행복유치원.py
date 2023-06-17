# 행복 유치원
# Gold 5, 그리디

n,k = map(int,input().split())
arr = tuple(map(int,input().split()))

cost = []
for i in range(n-1):
    cost.append(arr[i+1]-arr[i])

print(sum(sorted(cost)[:n-k]))