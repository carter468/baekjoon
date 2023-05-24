# 인공 신경망
# Gold 3, 수학

import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
arr1 = [[] for _ in range(m)]   # 인공 신경의 입력데이터 가중치 순서쌍
arr2 = [0]*m                    # 인공 신경의 편향값
for i in range(m):
    a = tuple(map(int,input().split()))
    c = a[0]
    for j in range(c):
        arr1[i].append((a[j+1]-1,a[j+c+1]))
    arr2[i] = a[-1]

a = tuple(map(int,input().split()))
arr3 = [0]*n                    # 각 입력데이터의 가중치 
b = a[-1]                       # 편향값
for i in range(m):
    for x,y in arr1[i]:
        arr3[x] += y*a[i]
    b += arr2[i]*a[i]
    
for _ in range(q):
    result = b
    for i,a in enumerate(map(int,input().split())):
        result += a*arr3[i]
    print(result)