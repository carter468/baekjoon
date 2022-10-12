# 펠린드롬 분할

s = input().strip()
n = len(s)

dp = [2500 for _ in range(n+1)]
dp[-1] = 0
ispelindrome = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):      # 길이 1 펠린드롬
    ispelindrome[i][i] = 1
for i in range(1,n):    # 길이 2 펠린드롬
    if s[i-1]==s[i]:
        ispelindrome[i-1][i] = 1
for i in range(3,n+1):  # i:펠린드롬길이
    for start in range(n-i+1):
        end = start+i-1
        if s[start]==s[end] and ispelindrome[start+1][end-1]:
            ispelindrome[start][end] = 1
for end in range(n):
    for start in range(end+1):
        if ispelindrome[start][end]:
            dp[end] = min(dp[end],dp[start-1]+1)
        else:
            dp[end] = min(dp[end],dp[end-1]+1)
print(dp[n-1])