# 로봇 프로젝트
# Gold 5, two pointer

import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())*10**7
        n = int(input())
        arr = sorted([int(input()) for _ in range(n)])

        l,r = 0,n-1
        while l < r:
            if arr[l]+arr[r] == x:
                print('yes',arr[l],arr[r])
                break
            if arr[l]+arr[r] < x:
                l += 1
            elif arr[l]+arr[r] > x:
                r -= 1
        else: print('danger')
    except:
        break