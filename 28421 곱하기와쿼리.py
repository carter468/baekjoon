# 곱하기와 쿼리
# Gold 5, math

import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = list(map(int,input().split()))

count = [0]*10001
for x in arr:
    count[x] += 1

for _ in range(q):
    a,b = map(int,input().split())
    if a == 2:
        b -= 1
        if arr[b] != 0:
            count[arr[b]] -= 1
            count[0] = 1
            arr[b] = 0
    else:
        if n == 1:
            print(0)
        elif b == 0:
            print(count[0])
        else:
            for i in range((b-1)//10000+1,int(b**0.5)+1):
                if count[i] == 0: continue
                if i*i == b:
                    if count[i] > 1:
                        print(1)
                        break
                elif b%i == 0 and count[b//i] > 0:
                    print(1)
                    break
            else: print(0)