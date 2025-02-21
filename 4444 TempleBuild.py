# Temple Build
# Platinum 5, DP

while True:
    try:
        h,a,b,*brick = map(int,input().split())
    except:
        break

    result = 0
    dp = [0]+[-1]*h
    for i in range(h+1):
        for x in brick:
            if i >= x and dp[i-x] >= 0:
                y = (b+(a-b)*(h-i)//h)//x
                dp[i] = max(dp[i],dp[i-x]+x**3*y**2)
        result = max(result,dp[i])
    print(result)