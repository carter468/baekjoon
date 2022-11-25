# 소수 사이 수열
# Silver 1, 수학

import sys
input = sys.stdin.readline

MAX = 1299710
prime = [True]*MAX
for i in range(2,int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i*2,MAX,i):
            prime[j] = False

for _ in range(int(input())):
    k = int(input())
    if prime[k]:
        print(0)
    else:
        for i in range(k+1,MAX):
            if prime[i]:
                right = i
                break
        for i in range(k-1,1,-1):
            if prime[i]:
                left = i
                break
        print(right-left)