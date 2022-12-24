# 가희는 그래플러야!!
# Gold 5, 기하학

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int,input().split()))
k = int(input())

c = 0
for i in range(1,n+1):
    if arr[i]/i==k:
        print('T')
        break
    elif arr[i]/i>k:
        if c==-1:
            print('T')
            break
        c = 1
    else:
        if c==1:
            print('T')
            break
        c = -1
else:
    print('F')