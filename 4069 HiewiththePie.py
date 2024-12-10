# Hie with the Pie
# Gold 4, floyd-warshall, bruteforcing

import itertools

while n:=int(input()):
    arr = [list(map(int,input().split())) for _ in range(n+1)]

    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])
    
    answer = 10**20
    for p in itertools.permutations(range(1,n+1)):
        temp = 0
        prev = 0
        for a in p:
            temp += arr[prev][a]
            prev = a
        answer = min(answer,temp+arr[prev][0])
    print(answer)