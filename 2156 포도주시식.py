# 포도주 시식

# n = 6
# wines = [6,10,13,9,8,1]
n = int(input())
wines = [0]*n
for i in range(n):
    wines[i] = int(input())
dp = [0] * n

if n==1:
    print(wines[0])
elif n==2:
    print(wines[0]+wines[1])
elif n==3:
    print(max(wines[0]+wines[1],wines[0]+wines[2],wines[1]+wines[2])) 
else:
    dp[0] = wines[0]
    dp[1] = wines[0]+wines[1]
    dp[2] = max(wines[0]+wines[1],wines[0]+wines[2],wines[1]+wines[2])
    dp[3] = max(dp[1]+wines[3],dp[0]+wines[2]+wines[3])

    for i in range(4,n):
        dp[i] = max(dp[i-2]+wines[i],dp[i-3]+wines[i-1]+wines[i],dp[i-4]+wines[i-1]+wines[i])

    print(max(dp[n-2],dp[n-1]))
