# 자물쇠
# Platinum 3, DP

N = int(input())
A = tuple(map(int,input()))
B = tuple(map(int,input()))

C = [(B[i]-A[i])%10 for i in range(N)]+[0,0]

dp = [[N]*10 for _ in range(10)]
dp[C[0]][C[1]] = 0
for i in range(N):
    ndp = [[N]*10 for _ in range(10)]
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    cost = 0
                    s = [a,b,C[i+2]]

                    diff = (s[2]-d)%10
                    cost += (min(diff,10-diff)+2)//3
                    for j in range(3):
                        s[j] = (s[j]-diff)%10
                    
                    diff = (s[1]-c)%10
                    cost += (min(diff,10-diff)+2)//3
                    for j in range(2):
                        s[j] = (s[j]-diff)%10

                    diff = s[0]
                    cost += (min(diff,10-diff)+2)//3

                    ndp[c][d] = min(ndp[c][d],dp[a][b]+cost)
    dp = ndp

print(dp[0][0])