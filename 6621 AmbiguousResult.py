# Ambiguous Result
# Gold 3, DP

def calc(a,op,b):
    if op == '*': return a*b
    if op == '+': return a+b

while (S:=input()) != 'END':
    num = []
    oper = []
    t = ''
    for c in S:
        if c in '+*':
            num.append(int(t))
            oper.append(c)
            t = ''
        else:
            t += c
    num.append(int(t))
    n = len(num)

    mindp = [[1<<63]*n for _ in range(n)]
    maxdp = [[0]*n for _ in range(n)]
    for i in range(n):
        mindp[i][i] = maxdp[i][i] = num[i]

    for l in range(2,n+1):
        for i in range(n-l+1):
            k = i+l-1
            for j in range(i+1,k+1):
                mindp[i][k] = min(mindp[i][k],calc(mindp[i][j-1],oper[j-1],mindp[j][k]))
                maxdp[i][k] = max(maxdp[i][k],calc(maxdp[i][j-1],oper[j-1],maxdp[j][k]))
    
    print(mindp[0][-1],maxdp[0][-1])