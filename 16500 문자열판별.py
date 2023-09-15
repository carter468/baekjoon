# 문자열 판별
# Gold 5, DP, string

def sol(idx):
    if idx == l:
        print(1)
        exit()
    if dp[idx] == 1: return
    dp[idx] = 1
    for a in arr:
        if l-idx >= len(a):
            for i in range(len(a)):
                if a[i] != s[idx+i]: break
            else: sol(idx+len(a))
    
s = input()
l = len(s)
arr = [input() for _ in range(int(input()))]

dp = [0]*(l+1)
sol(0)
print(0)