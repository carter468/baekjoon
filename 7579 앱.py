# 앱

n,m = 5,60
sizes = [30,10,20,35,40]
costs = [3,0,3,5,4]
n,m = map(int,input().split())
sizes = list(map(int,input().split()))
costs = list(map(int,input().split()))
ans = sum(costs)    

dp = [[0 for _ in range(ans+1)] for _ in range(n+1)]  

for i in range(n):              # i 번째까지 메모리에 대하여
    for j in range(1,ans+1):    # j 만큼의 코스트를 쓸때 최대 확보 메모리
        if costs[i] > j:        # 코스트가 더 큰 경우 
            dp[i+1][j] = dp[i][j]
        else:                   # 코스트를 쓸 수 있는 경우 
            dp[i+1][j] = max(dp[i][j] , dp[i][j-costs[i]] + sizes[i])
        if dp[i+1][j] >= m:     # 메모리 확보가 된 경우
            ans = min(ans,j)

print(ans)