# 양팔저울

n = int(input())
weights = [0]+list(map(int,input().split()))
q = int(input())
marbles = list(map(int,input().split()))

dp = [[0] * 40001 for _ in range(n+1)] # 구슬의 최대 무게 : 40000

for i in range(1,n+1): # i 번째 추까지 사용하여
    dp[i][weights[i]] = 1
    for j in range(1,40001): # 측정가능한 무게인가
        if dp[i-1][j] == 1:  # i-1번째 추까지 사용하여 j를 측정할 수 있다면
            dp[i][j] = 1                    # 아무것도 놓지 않는경우
            dp[i][abs(weights[i]-j)] = 1    # 양쪽에 놓는 경우
            dp[i][j+weights[i]] = 1         # 한쪽에 놓는 경우

for x in marbles:
    if dp[n][x]:
        print('Y',end=' ')
    else:
        print('N',end=' ')