# 내려가기
# Gold 5, DP

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp1 = list(arr[0])
dp2 = list(arr[0])

for i in range(1,n):
    dp11 = [0]*3
    dp22 = [10**9]*3
    for j in range(3):
        for k in (j-1,j,j+1):
            if 0 <= k < 3:
                dp11[j] = max(dp11[j],dp1[k]+arr[i][j])
                dp22[j] = min(dp22[j],dp2[k]+arr[i][j])
    dp1 = dp11
    dp2 = dp22
print(max(dp1),min(dp2))