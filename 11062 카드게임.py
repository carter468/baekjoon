# 카드게임
# Gold 3, 다이나믹프로그래밍, 게임이론

import sys
input = sys.stdin.readline

def game(turn,left,right):
    if left>right:
        return 0

    if dp[left][right]:
        return dp[left][right]
    
    if turn==0: # 근우는 최대 점수를 얻기위한 플레이를 한다.
        point = max(game(1,left+1,right)+cards[left],game(1,left,right-1)+cards[right])
        dp[left][right] = point
        return point
    else:   # 명우는 근우에게 최소점수를 주기위한 플레이를 한다.
        point = min(game(0,left+1,right),game(0,left,right-1))
        dp[left][right] = point
        return point

for _ in range(int(input())):
    n = int(input())
    cards = list(map(int,input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    game(0,0,n-1)
    print(dp[0][n-1]) 
