# 회색 영역
# Silver 1, 구현

import sys
input = sys.stdin.readline

while True:
    n,w = map(int,input().split())
    if n==0:
        break
    
    section = [0]*11    # 구간별 변량의 개수
    m = 0   
    for _ in range(n):
        x = int(input())
        section[x//w] += 1
        m = max(m,x)
    m //= w # 마지막 구간 확인

    amount_ink = 0
    for i in range(m):
        amount_ink += section[i]*(m-i)  # 구간별 넓이
    print(amount_ink/max(section)/m + 0.01)