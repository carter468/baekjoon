# 호기심
# Gold 2, 이분탐색, 소수판정, 누적 합

from bisect import bisect_left as bl, bisect_right as br 
import sys
input = sys.stdin.readline
END = 10**5

seive,prime,cso,cse,count = [1]*END,[],[0],[0],0
for i in range(2,END):
    if seive[i]:
        count += 1
        prime.append(i)
        if count%2: 
            if cso: 
                cso.append(cso[-1]+i)
            else: 
                cso.append(i)
        else: 
            if cse: 
                cse.append(cse[-1]+i)
            else: 
                cse.append(i)
        for j in range(i*i,END,i):
            seive[j] = 0

for _ in range(int(input())):
    a,b = map(int,input().split())
    a,b = bl(prime,a),br(prime,b)
    if a%2: 
        print((cse[b//2]-cse[a//2])*3-(cso[(b+1)//2]-cso[(a+1)//2]))
    else:   
        print((cso[(b+1)//2]-cso[(a+1)//2])*3-(cse[b//2]-cse[a//2]))