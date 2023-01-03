# 합이 같은 구간
# Gold 3, 누적 합

import sys
input = sys.stdin.readline

def solve(idx,target):
    j = 1
    while idx+j != m:
        k = seq[idx+j]-seq[idx]
        if k==target:
            idx += j
            j = 0
        elif k>target or idx+j==m-1:
            return 0
        j += 1
    return target

for _ in range(int(input())):
    m = int(input())
    seq = []
    for _ in range((m-1)//10+1):
        seq.extend(list(map(int,input().split())))
    for i in range(m-1):
        seq[i+1] += seq[i]
    for i in range(m):
        if seq[-1]%seq[i]==0:
            answer = solve(i,seq[i])
            if answer:
                print(answer)
                break