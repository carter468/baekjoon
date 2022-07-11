# 팰린드롬
import sys
input = sys.stdin.readline

# n = 7
# arr = [1,2,1,3,1,2,1]
# m = 4
# q = [[1,3],[2,5],[3,3],[5,7]]
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
q = []
for _ in range(m):
    q.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

def palindrome(i,j):
    if i==j or i>j:         # 마지막 하나 또는 더이상 검사할게 없을 경우
        return 1
    if arr[i] != arr[j]:    # 처음과 끝이 다르면 0
        return 0
    if dp[i+1][j-1] == 1:   # 양쪽에서 한칸씩 안쪽으로 검사하는데 팰린드롬인경우
        return 1
    else:
        return palindrome(i+1,j-1)  
    
for i in range(1,n+1):      # 길이가 i인 수열
    for j in range(n-i+1): # 시작지점
        dp[j][i+j-1] = palindrome(j,i+j-1)

for x in q:
    print(dp[x[0]-1][x[1]-1])