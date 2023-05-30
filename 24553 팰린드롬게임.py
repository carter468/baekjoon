# 팰린드롬 게임
# Gold 4, Ad hoc, 게임이론

import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    print(0 if n%10 else 1)