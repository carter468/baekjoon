# 1106 호텔

# import sys
# input = sys.stdin.readline

# c,n = map(int,input().split())
# table = []
# for _ in range(n):
#     table.append(list(map(int,input().split())))
# dp = [0]*1000
# for cost,customer in table:
#     dp[cost] = max(dp[cost],customer)
# for i in range(1,1000):
#     if dp[i] >= c:
#         print(i)
#         quit()
#     for j in range(1,i):
#         dp[i] = max(dp[i],dp[i-j]+dp[j])
#         if dp[i] >= c:
#             print(i)
#             quit()

import sys
input = sys.stdin.readline

c,n = map(int,input().split())
table = []
for _ in range(n):
    table.append(tuple(map(int,input().split())))
table.sort()

dp = [0]+[10**6]*(c+100)
ans = 10**6
for cost,customer in table:
    for i in range(customer,len(dp)):
        dp[i] = min(dp[i],dp[i-customer]+cost)
        if i>=c:
            ans = min(ans,dp[i])
print(ans)