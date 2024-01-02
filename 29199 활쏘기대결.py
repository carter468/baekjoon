# 활쏘기 대결
# Gold 2, DP, game theory

n = int(input())
arr = tuple(map(int,input().split()))

k = arr[0]
result = max(0,k)
for i in range(1,n):
    k += arr[i]
    result = max(result,k-result)
print(result)