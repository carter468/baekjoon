# 최대 최소공배수
# Gold 4, greedy

import sys
input = sys.stdin.readline

def lcm(a,b):
    c = a*b
    while b:
        a,b = b,a%b
    return c//a

for _ in range(int(input())):
    n = int(input())
    a = lcm(n-1,n-2)
    if n%2 == 0:
        print(max(lcm(a,n-3),lcm(a,n),lcm(lcm(n-3,n-1),n)))
    else:
        print(max(lcm(a,n-3),lcm(a,n),lcm(lcm(n-3,n-2),n)))