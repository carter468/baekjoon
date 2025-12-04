# Autobiography
# Gold 4, combinatorics

import sys
input = sys.stdin.readline

while True:
    try:
        N,M = map(int,input().split())
        C = input()
        count = [0]*(N+1)
        edge = []
        for _ in range(M):
            a,b = map(int,input().split())
            if C[a-1] != C[b-1]:
                count[a] += 1
                count[b] += 1
                edge.append((a,b))
        
        result = 0
        for a,b in edge:
            result += (count[a]-1)*(count[b]-1)
        print(result)

    except:
        break