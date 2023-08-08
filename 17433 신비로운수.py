# 신비로운 수
# Gold 5, math

import sys
input = sys.stdin.readline

def GCD(a,b):
    while b != 0:
        a,b = b,a%b
    return a
    
for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int,input().split()))

    dif = set()
    for i in range(n):
        dif.add(abs(arr[i]-arr[i-1]))
    result = abs(arr[0]-arr[1])
    for x in dif:
        result = GCD(result,x)

    print(result if result else 'INFINITY')