# 좋은 수열
# Gold 4, backtracking

def solve(l):
    for i in range(1,l//2+1):
        if result[-i:] == result[-i*2:-i]: return
    if l == n:
        print(''.join(result))
        exit()
    for i in ('1','2','3'):
        result.append(i)
        solve(l+1)
        result.pop()

n = int(input())

result = ['1']
solve(1)