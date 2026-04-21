# 숌 사이 수열
# Gold 5, bruteforcing, bacaktracking

def solve(result):
    l = len(result)
    if l == N:
        exit(print(*result))
    
    for x in X:
        c = result.count(x)
        if c == 0 or (c == 1 and l-result.index(x)-1 == x):
            result.append(x)
            solve(result)
            result.pop()

N = int(input())*2
X = sorted(map(int,input().split()))

solve([])
print(-1)