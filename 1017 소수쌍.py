# 소수 쌍

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num1 = [0]
num2 = [0]
prime = [1]*2000
answer = []
for i in range(2,46):   # 소수찾기
    if prime[i] == 1:
        for j in range(i*2,2000,i):
            prime[j] = 0
for i in range(n):      # 홀수그룹 짝수그룹 나누기 첫번째 숫자는 1번그룹
    if num[i]%2 == num[0]%2:
        num1.append(num[i])
    else:
        num2.append(num[i])
s = [[] for _ in range(len(num1))]
for i in range(1,len(num1)):    # 1번그룹숫자에 대해 짝 찾기
    for j in range(1,len(num2)):
        if prime[num1[i]+num2[j]]:
            s[i].append(j)
def dfs(idx):           # 이분매칭
    if visit[idx] == 1:
        return 0
    visit[idx] = 1
    for i in s[idx]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = idx
            return 1
    return 0
for i in s[1]:
    d = [0]*len(num2)
    d[i] = 1
    cnt = 1
    for j in range(1,len(num1)):
        visit = [0]*len(num1)
        visit[1] = 1
        cnt += dfs(j)
    if cnt == n//2:
        answer.append(num2[i])
if not answer:
    print(-1)
else:
    print(*sorted(answer))