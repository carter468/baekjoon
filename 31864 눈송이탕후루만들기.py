# 눈송이 탕후루 만들기
# Gold 3, binary search, hash set

from collections import defaultdict
import sys,bisect
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

n,m = map(int,input().split())
dic1 = defaultdict(list)
dic2 = defaultdict(list)
for _ in range(n):
    a,b = map(int,input().split())
    g = gcd(a,b)
    if a == 0:
        if b > 0: dic1['inf'].append(b)
        else: dic2['inf'].append(-b)
    elif a > 0: dic1[(a//g,b//g)].append(a)
    else: dic2[(a//g,b//g)].append(-a)
for a in dic1:
    dic1[a].sort()
for a in dic2:
    dic2[a].sort()

result = 0
for _ in range(m):
    a,b = map(int,input().split())
    g = gcd(a,b)
    if a == 0:
        if b > 0:
            result = max(result,bisect.bisect_left(dic1['inf'],b+1))
        else:
            result = max(result,bisect.bisect_left(dic2['inf'],-b+1))
    elif a > 0:
        result = max(result,bisect.bisect_left(dic1[(a//g,b//g)],a+1))
    else:
        result = max(result,bisect.bisect_left(dic2[(a//g,b//g)],-a+1))
print(result)