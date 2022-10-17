# 상어의 저녁식사

import sys
input = sys.stdin.readline

n = int(input())
shark = []
for _ in range(n):
    shark.append(list(map(int,input().split())))
shark.sort(reverse=True)
foodchain = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            foodchain[i].append(j)      # i번째 상어가 먹을 수 있는 상어

def dfs(idx):   # 이분매칭
    if visit[idx]:
        return False
    visit[idx] = 1
    for next in foodchain[idx]:
        if matching[next] == -1:
            matching[next] = idx
            return True
        else:
            prev = matching[next]
            if dfs(prev):           
                matching[next] = idx
                return True
    return False

matching = [-1]*n
for _ in range(2):
    for i in range(n):
        visit = [0]*n
        dfs(i)
print(matching.count(-1))