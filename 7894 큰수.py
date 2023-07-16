# 큰 수
# Gold 3, math

import sys,math
input = sys.stdin.readline

for _ in range(int(input())):
    result = 0
    for i in range(2,int(input())+1):
        result += math.log10(i)
    print(int(result)+1)