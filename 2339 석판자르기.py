# 석판 자르기
# Gold 1, divide and conquer

def solve(a,b,c,d,e):
    def isvalid(q):
        if q == 1:
            for k in range(c,d):
                if A[i][k] == '2': return False
        else:
            for k in range(a,b):
                if A[k][j] == '2': return False
        return True

    if (a,b,c,d,e) in dp: return dp[(a,b,c,d,e)]

    y = 0
    gem = 0
    cut = False
    for i in range(a,b):
        for j in range(c,d):
            if A[i][j] == '1':
                if e != 1 and isvalid(1):
                    y += solve(a,i,c,d,1)*solve(i+1,b,c,d,1)
                if e != 2 and isvalid(2):
                    y += solve(a,b,c,j,2)*solve(a,b,j+1,d,2)
                cut = True
            elif A[i][j] == '2':
                gem += 1

    if not cut and gem == 1: y = 1
    dp[(a,b,c,d,e)] = y
    return y

N = int(input())
A = [input().split() for _ in range(N)]

dp = dict()
result = solve(0,N,0,N,0)
print(result if result > 0 else -1)