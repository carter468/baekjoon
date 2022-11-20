# 통학경로
# Silver 1, 다이나믹 프로그래밍

a,b = map(int,input().split())  
c = [tuple(map(int,input().split())) for _ in range(int(input()))]

answer = [[0 for _ in range(b+1)] for _ in range(a+1)]
if (1,1) not in c:
    answer[1][1] = 1

for i in range(1,a+1):
    for j in range(1,b+1):
        if (i,j) == (1,1):
            continue
        if (i,j) not in c:
            answer[i][j] = answer[i-1][j]+answer[i][j-1]
print(answer[a][b])
