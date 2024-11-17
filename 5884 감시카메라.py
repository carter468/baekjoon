# 감시 카메라
# Gold 4, bruteforcing, backtracking

import sys
sys.setrecursionlimit(55555)
input = sys.stdin.readline

def solve(count):
    if len(line) > 3: return
    
    if count == n:
        print(1)
        exit()
    
    x,y = arr[count]
    for a,b in line:
        if x == a or y == b:
            solve(count+1)
            break
    else:
        line.append((x,-1))
        solve(count+1)
        line.pop()
        line.append((-1,y))
        solve(count+1)
        line.pop()

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

line = []
solve(0)
print(0)