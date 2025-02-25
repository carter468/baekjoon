# 쉐이드 커튼 위 먼지는 쌓이는 중
# Gold 4, ad hoc

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

count = [[0]*2001 for _ in range(M)]
for i in range(N):
    for j in range(M):
        count[j][arr[i][j]] += 1

result = [[0,0] for _ in range(M)]
for i in range(M):
    for j in range(1,2001):
        if result[i][0] < count[i][j]:
            result[i] = [count[i][j],j]

v = [0]*M
x = (2000,0)
answer = []
for i in range(M):
    v[i] = result[i][0]
    answer.append(result[i][1])
    if v[i] < x[0]: x = (v[i],i)

for i in range(M):
    if i == x[1]: continue
    if v[i] != N:
        for j in range(N):
            if answer[i] != arr[j][i]:
                answer[x[1]] = arr[j][x[1]]
                break
        break
else:
    for j in range(2001):
        if count[x[1]][j] == 0:
            answer[x[1]] = j
            break

print(*answer)