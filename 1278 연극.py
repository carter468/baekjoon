# 연극
# Gold 3, recursion

def solve(n):
    if n == 0: return
    solve(n-1)
    print(n)
    solve(n-1)

N = int(input())

print((1<<N)-1)
solve(N)
print(N)