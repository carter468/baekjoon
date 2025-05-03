# N으로 만들기
# Gold 4, backtracking

def solve(x,arr):
    if len(x) == 1:
        result.add(tuple(arr))
        return
    
    a,b = x[1:],x[:-1]
    solve(a,arr+[a])
    solve(b,arr+[b])

N = input()

result = set()
solve(N,[N])
print(len(result))