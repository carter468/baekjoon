#전깃줄

# n = 8
# lines = [[1,8],[3,9],[2,2],[4,1],[6,4],[10,10],[9,7],[7,6]]
# n = 5
# lines = [[1,3],[3,1],[2,5],[4,6],[6,4]]
# crossing = [[0] for _ in range(n)]
# cnt = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if (lines[i][0]-lines[j][0]) * (lines[i][1]-lines[j][1]) < 0:   
#             crossing[i][0] = lines[i][0]     # 겹친 횟수
#             crossing[j][0] = lines[j][0]
#             crossing[i].append(lines[j][0])  # 겹친 줄의 왼쪽줄번호
#             crossing[j].append(lines[i][0])
#             cnt += 2
# crossing.sort(key=len)  # 길이순으로 정렬하면 마지막 리스트가 가장 많이겹치는줄

# ans = 0
# while cnt != 0:     # 겹치는 수가 0이 될때까지
#     for i in range(1,len(crossing[-1])):    # 마지막리스트의 겹치는 줄번호들을
#         for x in crossing[:-1]:             # 나머지 리스트와 비교
#             if crossing[-1][i] == x[0]:     # 그 줄번호가 맞다면
#                 cnt -= 2                    #겹친 줄을 제거하면서 겹치는수 -2
#     ans += 1    #1개 제거
#     crossing.pop()      # 제거된 줄 
# print(ans)

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))

#왼쪽 번호 기준 정렬 후 오른쪽 번호의 LIS 구하기 : 서로 겹치지 않는 줄의 개수
lines.sort()
dp = [0]*n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))        # 총 개수에서 겹치지 않는 줄의 개수를 빼면 제거해야하는 줄의 수이다