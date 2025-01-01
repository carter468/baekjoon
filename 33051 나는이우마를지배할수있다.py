# 나는 이 우마를 지배할 수 있다
# Gold 5, bruteforcing

import sys
input = sys.stdin.readline

N,K,M = map(int,input().split())
score = [0]*5
count = [[0]*4 for _ in range(5)]
for _ in range(N):
    arr = tuple(map(int,input().split()))
    for i in range(4):
        score[arr[i]] += arr[i+4]
        count[arr[i]][i] += 1

for d1 in range(-100,101):
    for d2 in range(-100,d1+1):
        for d3 in range(-100,d2+1):
            d4 = -d1-d2-d3
            if d4 < -100 or 100 < d4 or d4 > d3: continue
            result = []
            for i in range(1,5):
                s = score[i]+count[i][0]*d1+count[i][1]*d2+count[i][2]*d3+count[i][3]*d4
                result.append((-s,i))
            result.sort()
            if result[M-1][1] == K:
                print(d1,d2,d3,d4)
                exit()
print(-1)