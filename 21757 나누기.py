# 나누기
# Gold 2, prefix sum, DP

N = int(input())
arr = list(map(int,input().split()))
for i in range(N-1):
    arr[i+1] += arr[i]

if arr[-1]%4 != 0: exit(print(0))
k = arr[-1]//4
count = [1,0,0,0]
for i in range(N-1):
    for j in range(2,-1,-1):
        if arr[i] == k*(j+1): count[j+1] += count[j]
print(count[3])