# 산업 스파이의 편지
# Gold 5, bruteforcing

def solve(state,x):
    if state+1 == 1<<b: return
    for i in range(b):
        if state>>i&1: continue
        nx = x+a[i]
        if seive[int(nx)]: result.add(int(nx))
        solve(state|(1<<i),nx)

M = 10**7
seive = [False,False]+[True]*M
for i in range(2,int(M**0.5)+1):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False

for _ in range(int(input())):
    a = input()
    b = len(a)
    result = set()
    solve(0,'')
    print(len(result))