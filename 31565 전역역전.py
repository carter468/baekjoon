# 전역 역전
# Gold 4, DP, knapsack, implementation

def f():
    def ly(y):
        return (y%100 != 0 and y%4 == 0) or y%400 == 0
    
    month = [0,31,28,31,30,31,30,31,31,30,31,30]

    Y,M,D = map(int,input().split())

    x = 365*(Y-1)
    for i in range(Y):
        if ly(i): x += 1
    
    x += sum(month[:M])
    if ly(Y) and M > 2: x += 1

    x += D

    return x

d1,d2 = f(),f()
T,N = map(int,input().split())
arr = []
for _ in range(N):
    a,b,c = map(int,input().split())
    if a == 3: arr.append((b,c*30))
    else: arr.append((b,c))

dp = [0]*(T+1)
for w,v in arr:
    for i in range(T,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)

print(abs(d1+dp[T]-d2))