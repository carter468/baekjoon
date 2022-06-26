#쉬운 계단 수

# 점화식을 구하기 위한 코드
# n = 3           #자리 수
# number_stair = [[] for _ in range(n)]
# number_stair[0] = [1,2,3,4,5,6,7,8,9]   #한 자리수 초기화

# for i in range(1,n):
#     for j in number_stair[i-1]:
#         if j % 10 == 0:
#             number_stair[i].append(j*10 + 1)
#         elif j % 10 == 9:
#             number_stair[i].append(j*10 + 8)
#         else:
#             number_stair[i].append(j*10 + j%10 + 1)
#             number_stair[i].append(j*10 + j%10 - 1)

# print(number_stair[n-1],len(number_stair[n-1]))

# 끝자리의 개수를 이용하여 점화식을 세우기
# j = 0 : dp[i][j] = dp[i-1][1] , j = 9 : dp[i][j] = dp[i-1][8]
            # j = 1~8 : dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] 
# n = int(input())
# dp = [[0 for _ in range(10)] for _ in range(n)] # 끝자리수의 개수를 저장할 리스트
# dp[0] = [0,1,1,1,1,1,1,1,1,1]   # 1자리 계단수의 끝자리수 개수
# for i in range(1,n):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][8]
#         else:
#             dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % 1000000000

# print(sum(dp[n-1])%1000000000)