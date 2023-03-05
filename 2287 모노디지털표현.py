# 모노디지털 표현
# Gold 1, dp

import sys
input = sys.stdin.readline

k = int(input())

dp = [set() for _ in range(9)]
for i in range(1,9):
    dp[i].add(k*int('1'*i))
    for j in range(1,i):
        for num1 in dp[j]:
            for num2 in dp[i-j]:
                dp[i].add(num1+num2)
                dp[i].add(num1*num2)
                dp[i].add(abs(num1-num2))
                if num2!=0:
                    dp[i].add(num1//num2)

for _ in range(int(input())):
    a = int(input())
    for i in range(1,9):
        if a in dp[i]:
            print(i)
            break
    else:
        print('NO')