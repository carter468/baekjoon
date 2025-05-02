# 주사위 쌓기
# Gold 5, implementation, bruteforcing

import sys
input = sys.stdin.readline

def f(top,idx):
    a,b,c,d,e,f = arr[idx]
    if top == a: return max(b,c,d,e),f
    elif top == b: return max(a,c,e,f),d
    elif top == c: return max(a,b,d,f),e
    elif top == d: return max(a,c,e,f),b
    elif top == e: return max(a,b,d,f),c
    elif top == f: return max(b,c,d,e),a

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

result = 0
for top in range(1,7):
    x = 0
    for i in range(N):
        m,top = f(top,i)
        x += m
    result = max(result,x)
print(result)