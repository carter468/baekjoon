# 치킨 먹고 싶다
# Gold 3, math

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p,m,f,c = map(int,input().split())

    sang = m//p
    coupon = sang*c
    doo = sang+coupon//f
    if coupon >= f:
        coupon -= f
        sang += 1+coupon//(f-c)

    print(sang-doo)