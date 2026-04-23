# Match Maker
# Platinum 1, stable marriage

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    M = [0]+[tuple(map(int,input().split())) for _ in range(N)]
    W = [0]+[tuple(map(int,input().split())) for _ in range(N)]

    rank = [[0]*(N+1) for _ in range(N+1)]
    for w in range(1,N+1):
        for r,m in enumerate(W[w]):
            rank[w][m] = r

    next_idx = [0]*(N+1)
    woman_of_man = [-1]*(N+1)
    man_of_woman = [-1]*(N+1)
    free_men = list(range(1,N+1))
    while free_men:
        m = free_men.pop()
        w = M[m][next_idx[m]]
        next_idx[m] += 1

        if man_of_woman[w] == -1:
            man_of_woman[w] = m
            woman_of_man[m] = w
        else:
            current = man_of_woman[w]
            if rank[w][m] < rank[w][current]:
                man_of_woman[w] = m
                woman_of_man[m] = w
                woman_of_man[current] = -1
                free_men.append(current)
            else:
                free_men.append(m)

    print(*woman_of_man[1:])