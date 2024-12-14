# 약속 장소
# Gold 5, bruteforcing

def check(t):
    for i in range(1,N):
        c = 0
        for j in range(L):
            if t[j] != arr[i][j]: c += 1
        if c > 1: return False
    return True

def solve():
    for i in range(L):
        for j in range(26):
            t = list(arr[0])
            t[i] = chr(j+65)
            if check(t): return ''.join(t)
    return 'CALL FRIEND'

N,L = map(int,input().split())
arr = [input() for _ in range(N)]
print(solve())