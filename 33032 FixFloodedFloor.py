# Fix Flooded Floor
# Gold 3, greedy

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    grid = [list(input()) for _ in range(2)]

    result = 'Unique'
    for i in range(N):
        if grid[0][i]+grid[1][i] == '..':
            if i != N-1 and grid[0][i+1]+grid[1][i+1] == '..':
                result = 'Multiple'
        elif grid[0][i] == '.':
            if grid[0][i+1] != '.': return 'None'
            grid[0][i+1] = '#'
        elif grid[1][i] == '.':
            if grid[1][i+1] != '.': return 'None'
            grid[1][i+1] = '#'
    return result

for _ in range(int(input())):
    print(solve())