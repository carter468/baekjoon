# 가운데를 말해요

import heapq
import sys
input = sys.stdin.readline

leftheap = []   # -1을 곱한 최소힙으로 leftheap[0] 에 중간값 * -1 이 있다.
rightheap = []  # 입력값 그대로의 최소힙으로 rightheap[0] 에 중간값 이 있다.

n = int(input())
location = -1        # 왼쪽 = -1 , 오른쪽 = 1
for _ in range(n):
    x = int(input())
    if location == -1:   # 왼쪽 차례
        heapq.heappush(leftheap,x*location)
        location *= -1
    else:                #오른쪽 차례
        heapq.heappush(rightheap,x*location)
        location *= -1
    if rightheap and leftheap[0] * -1 > rightheap[0]: # 중간값 비교 후 교환
        left = heapq.heappop(rightheap) * -1
        right = heapq.heappop(leftheap) * -1
        heapq.heappush(leftheap,left)
        heapq.heappush(rightheap,right)
    
    print(leftheap[0]*-1)