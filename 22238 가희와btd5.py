# 가희와 btd5
# Gold 5, 이분탐색

import sys
input = sys.stdin.readline

def gcd(a,b):
    a,b = abs(a),abs(b)
    while b != 0:
        a,b = b,a%b
    return a

def change(x,y):
    if x == 0:
        y = (y > 0)-(y < 0)
    elif y == 0:
        x = (x > 0)-(x < 0)
    else:
        g = gcd(x,y)
        x //= g
        y //= g
    return x,y

def bs(target):
    left,right = 0,n-1
    while left <= right:
        mid = (left+right)//2
        if hp[mid] <= target:
            left = mid+1
        else:
            right = mid-1
    return left

n,m = map(int,input().split())
x,y,h = map(int,input().split())
x,y = change(x,y)
hp = sorted([h]+[list(map(int,input().split()))[2] for _ in range(n-1)])

damage = 0
for _ in range(m):
    a,b,d = map(int,input().split())
    a,b = change(a,b)
    if (x,y) == (a,b):
        damage += d
    print(n-bs(damage))