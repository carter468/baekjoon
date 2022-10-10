# 택배 기사 민서

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):          # 1 -> -1 -> 2 -> -2 -> 4 -> -4 와 같은 규칙으로 배달
    x = int(input())
    for i in range(40):
        if abs(x) <= 2**i:  # 2**i까지 배달하는 길에 x가 있다
            break
    ans = 2**(i+2) - 4      # 2**(i-1)*(-1) 까지 배달하고 원점으로 돌아온 총 거리
    if x >= 0:              # x까지 간다
        ans += x
    else:                   # 2**i 만큼 더 가고 원점으로 갔다가 다시 반대로 x까지 간다
        ans += 2**(i+1) - x
    sys.stdout.write(str(ans)+'\n')