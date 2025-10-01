# Rig Placement
# Gold 5, DP, knapsack

for ds in range(int(input())):
    N,M,B = map(int,input().split())
    arr = [tuple(map(float,input().split())) for _ in range(N)]

    dp = [0]*(B+1)
    for i in range(N):
        for j in range(B,-1,-1):
            for k in range(min(M,j)+1):
                dp[j] = max(dp[j],dp[j-k]+arr[i][k])
    print(f'Data Set {ds+1}:')
    print(f'{dp[B]+1e-9:.2f}')
    print()