# The Tower of Babylon
# Gold 4, DP

import sys
input = sys.stdin.readline

t = 1
while N := int(input()):
    arr = set()
    for _ in range(N):
        a,b,c = sorted(map(int,input().split()))
        arr.add((a,b,c))
        arr.add((a,c,b))
        arr.add((b,c,a))
    arr = sorted(arr)

    n = len(arr)
    dp = [0]*n
    for i in range(n):
        m = 0
        for j in range(i):
            if arr[j][0] < arr[i][0] and arr[j][1] < arr[i][1]:
                m = max(m,dp[j])
        dp[i] = m+arr[i][2]
    print(f'Case {t}: maximum height = {max(dp)}')
    t += 1