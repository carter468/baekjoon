# 급식 배식
# Gold 5, DP

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
food = [[] for _ in range(n+1)] # i번 음식을 배식받을 수 있는 (학생번호, 만족도) 저장
for i in range(1,m+1):
    a = tuple(map(int,input().split()))
    for j in range(a[0]):
        food[a[j*2+1]].append((i,a[j*2+2]))

result = 0
for i in range(1,n+1): # 각 음식에 대해서 dp로 최대만족도 구하기
    l = len(food[i]) # i번 음식을 배식받을 수 있는 학생 수
    dp = [[0]*2 for _ in range(l+1)] # [배식 안받기, 배식 받기]
    for j in range(l):
        dp[j+1][0] = max(dp[j]) # 배식 안받기
        # 배식 받기
        if food[i][j][0] == food[i][j-1][0]+1: # 전사람과 1번차이 나는 경우 
            dp[j+1][1] = dp[j][0]+food[i][j][1]
        else:
            dp[j+1][1] = max(dp[j])+food[i][j][1]
    result += max(dp[-1])
print(result)