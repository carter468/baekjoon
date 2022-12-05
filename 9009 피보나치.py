# 피보나치
# Silver 1, 그리디 알고리즘

import sys
input = sys.stdin.readline

# 10**9 이하의 피보나치 수열
MAX = 43
fibo = [0]*MAX
fibo[:2] = [1,2]
for i in range(2,MAX):
    fibo[i] = fibo[i-1]+fibo[i-2]

for _ in range(int(input())):
    n = int(input())
    answer = []
    idx = MAX-1
    while n:
        if fibo[idx] > n:
            idx -= 1    
        else:   # n이하의 가장 큰 피보나치 수를 넣어준다.
            answer.append(fibo[idx])
            n -= fibo[idx]
            idx -= 2    # 연속된 피보나치 수의 합은 다음 피보나치 수이므로 답이 될 수 없다.
    print(*answer[::-1])