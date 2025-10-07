# Prime Median
# Gold 5, seive, prefix sum

import sys
input = sys.stdin.readline

M = 1_000_001
seive = [True]*M
for i in range(2,int(M**0.5)):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False

pos = dict()
psum = [0,0]
for i in range(2,M):
    psum.append(psum[-1]+seive[i])
    if seive[i]:
        pos[psum[-1]] = i

for _ in range(int(input())):
    a,b = map(int,input().split())
    count = psum[b]-psum[a-1]
    if count%2 == 0:
        print(-1)
    else:
        print(pos[psum[a-1]+count//2+1])