# Discounts
# Gold 5, DP, knapsack

M = 500

while True:
    try:
        print(input())
        PD,PC = map(int,input().split())

        price = PD*100+PC
        dp = [10**9]*M
        dp[0] = 0

        arr = [(1,price)]
        for _ in range(int(input())):
            b,f = map(int,input().split())
            arr.append((b+f,b*price))
        
        for i in range(M):
            for b,p in arr:
                if i >= b: dp[i] = min(dp[i],dp[i-b]+p)
        
        for i in range(M-1,-1,-1):
            if dp[i-1] > dp[i]: dp[i-1] = dp[i]

        for _ in range(int(input())):
            x = int(input())
            y = x*price-dp[x]
            print(f'Buy {x}, save ${y//100}.{y%100:02}')

        input()
        print()
        
    except: break