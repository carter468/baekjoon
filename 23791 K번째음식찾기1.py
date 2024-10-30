# K번째 음식 찾기 1
# Gold 3, binary search

import sys
input = sys.stdin.readline

def find(arr,x,r):
    lo,hi = -1,r
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] > x: hi = mid
        else: lo = mid
    return hi

input()
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

for _ in range(int(input())):
    i,j,k = map(int,input().split())
    lo,hi = 0,1<<31
    while True:
        mid = (lo+hi)//2
        a = find(A,mid,i)
        b = find(B,mid,j)
        if a+b == k:
            if A[a-1] == mid:
                print(1,a)
                break
            if B[b-1] == mid:
                print(2,b)
                break
        if a+b >= k: hi = mid
        else: lo = mid