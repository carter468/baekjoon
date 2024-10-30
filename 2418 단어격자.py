# 단어 격자
# Gold 4, DP

h,w,l = map(int,input().split())
arr = [input() for _ in range(h)]
s = input()

dp = [[[0]*w for _ in range(h)] for _ in range(l+1)]
for i in range(l):
    for j in range(h):
        for k in range(w):
            if arr[j][k] == s[i]:
                if i == 0:
                    dp[i+1][j][k] = 1
                else:
                    for x,y in (j+1,k),(j+1,k+1),(j+1,k-1),(j,k+1),(j,k-1),(j-1,k),(j-1,k+1),(j-1,k-1):
                        if 0 <= x < h and 0 <= y < w:
                            dp[i+1][j][k] += dp[i][x][y]

result = 0
for i in range(h):
    for j in range(w):
        result += dp[l][i][j]
print(result)