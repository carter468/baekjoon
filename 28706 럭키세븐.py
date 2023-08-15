# 럭키 세븐
# Gold 5, DP

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = {1}
    for _ in range(int(input())):
        temp = set()
        a,b,c,d = input().split()
        for i in result:
            if a == '+': temp.add((i+int(b))%7)
            else: temp.add((i*int(b))%7)
            if c == '+': temp.add((i+int(d))%7)
            else: temp.add((i*int(d))%7)
        result = temp
    print('LUCKY' if 0 in result else 'UNLUCKY')