# 나머지계산
# Silver 2, 정수론

import sys
input = sys.stdin.readline

# b의 거듭제곱을 b-1로 나눈 나머지는 항상 1임을 이용
for _ in range(int(input())):
    b,d = map(str,input().split())
    print(sum(list(map(int,d)))%(int(b)-1))