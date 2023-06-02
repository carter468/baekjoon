# 카카오톡
# Gold 4, 수학

from collections import defaultdict
import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
    
user = defaultdict(int)
n = int(input())
for _ in range(n):
    a,b,_ = map(int,input().split())
    g = gcd(a,b)
    user[(a//g,b//g)] += 1

result = n*(n-1)
for a in user.values():
    result -= a*(a-1)
print(result//2)