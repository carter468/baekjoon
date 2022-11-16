# 스테판 쿼리
# Silver 5, 구현,시뮬레이션

def game(a,b):
    if a==b:
        return 0
    if a==1:
        if b==2:
            return -1
        else:
            return 1
    if a==2:
        if b==3:
            return -1
        else:
            return 1
    if a==3:
        if b==1:
            return -1
        else:
            return 1

n = int(input())
team_a = list(map(int,input().split()))
team_b = list(map(int,input().split()))

answer = 0  # 연승기록
winning_streak = 1  # 현재 연승
winning_team = game(team_a[0],team_b[0]) # 첫경기 승리팀 1:Team A, -1:Team B 
for i in range(1,n):
    result = game(team_a[i],team_b[i])  # 게임결과
    if result == winning_team:    # 연승
        winning_streak += 1
    else:   # 연승끊김
        answer = max(answer,winning_streak)
        winning_team *= -1
        winning_streak = 1
print(max(answer,winning_streak))