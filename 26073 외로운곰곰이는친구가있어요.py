# 외로운 곰곰이는 친구가 있어요
# Gold 3, number theory

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

for _ in range(int(input())):
    x,y = map(int,input().split())
    _,*A = map(int,input().split())
    
    g = 0
    for a in A:
        g = gcd(g,a)
    if x%g == 0 and y%g == 0: print('Ta-da')
    else: print('Gave up')