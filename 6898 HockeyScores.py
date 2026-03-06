# Hockey Scores
# Platinum 5, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        a,b = map(int,input().split('-'))
        arr.append((min(a,b),max(a,b)))

    games = []
    for a,b in sorted(arr):
        best = -1,-1
        for i in range(len(games)):
            j = games[i][-1][1]
            if j <= b and j > best[0]:
                best = j,i
        if best[1] != -1:
            games[best[1]].append((a,b))
        else:
            games.append([(a,b)])
    
    print(len(games))
    print(*[' '.join(f'{a}-{b}' for a,b in game) for game in games],sep='\n')