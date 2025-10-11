# 알록달록 초콜릿 만들기
# Gold 2, math, binary search

import sys
input = sys.stdin.readline

def check(x):
    return (x*3+5)*x//2+1 >= N

for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(1)
        continue

    # 몇번째 군에 있는가?
    # i번째 군까지의 개수가 N보다 크거나 같은 가장 작은 i가 속해있는 군이다.
    lo,hi = 0,N
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid
    a = (lo*3+5)*lo//2+1 # lo번째 군까지의 개수
    b = a*3-2 # lo번째 군의 마지막 수

    # hi번째 군 각 행의 항의 개수 = hi개,hi+1개,hi개
    if N <= a+hi: # 1행에 있다.
        print(b+3*(N-a)+1)
    else: # 2,3행에 있다.
        print(b+3*(N-a))