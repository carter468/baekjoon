# 3교시: 수학
# Gold 5, backtracking

def solve(x,c):
    if x == 1: return
    if c == N:
        result.add(x)
        return

    if x > 3 and (x-1)%3 == 0 and ((x-1)//3)%2 == 1:
        solve((x-1)//3,c+1)
    solve(x*2,c+1)

N = int(input())
if N == 1: exit(print(1,1,sep='\n'))

result = set()
solve(2,2)
print(len(result))
if result: print(*sorted(result),sep='\n')