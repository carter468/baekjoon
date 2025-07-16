# If I Could Turn Back Time
# Gold 4, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    H = tuple(map(int,input().split()))
    P = tuple(map(int,input().split()))

    arr = []
    for i in range(N):
        if H[i] > P[i]:
            print(-1)
            break
        arr.append((H[i],P[i]))
    else:
        result = 0
        k = 0
        for a,b in sorted(arr):
            if b-a < k:
                result = -1
                break
            result += b-a-k
            k = b-a
        print(result)