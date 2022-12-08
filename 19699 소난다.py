# 소-난다!
# Silver 2, 백트래킹 

prime = [True]*9001
prime[1] = False
for i in range(2,int(9001**0.5)+1):
    if prime[i]:
        for j in range(i+i,9001,i):
            prime[j] = False

def fly(w,c):
    if c==m:
        if prime[w]:
            answer.append(w)
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            fly(w+weight[i],c+1)
            visit[i] = False

n,m = map(int,input().split())
weight = list(map(int,input().split()))
visit = [False]*n
answer = []
fly(0,0)
if answer:
    print(*sorted(set(answer)))
else:
    print(-1)