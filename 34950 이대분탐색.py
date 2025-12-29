# 이대 분 탐색
# Gold 1, greedy, recursion, constructive

def solve(s,c):
    if c == 1: return
    a = c//2
    result.extend(range(s,s+a))
    solve((s+L)//2+1,c-a)

N,L = map(int,input().split())

if N == L+1:
    print(*range(L+1))
else:
    result = []
    solve(0,N)
    print(*result,L)