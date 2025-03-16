# 합집합
# Gold 5, bruteforcing

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = [set(tuple(map(int,input().split()))[1:]) for _ in range(int(input()))]
    
    union = set()
    for a in arr:
        union |= a

    result = 0
    for x in union:
        cur = set()
        for a in arr:
            if x not in a:
                cur |= a
        if len(cur) < len(union):
            result = max(result,len(cur))
            
    print(result)