# 계산 문제
# Gold 1, 브루트포스 알고리즘, 깊이 우선 탐색, 문자열, 비트마스킹

import sys
sys.setrecursionlimit(10**9)

def dfs(e,t,n):
    if n==len(e)-1:
        if eval(t)==2000:
            result.append(t)
        return
    dfs(e,t+'+'+e[n+1],n+1)
    dfs(e,t+'-'+e[n+1],n+1)
    dfs(e,t+'*'+e[n+1],n+1)

s = input()
l = len(s)

p = []
for i in range(1<<l):
    e = []
    temp = ''
    for j in range(l):
        temp += s[j]
        if i&(1<<j):
            if len(temp)>1 and temp[0]=='0':
                break
            else:
                e.append(temp)
                temp = ''
    
    if temp and len(temp)<6 and (len(temp)==1 or temp[0]!='0'):
        e.append(temp)
        p.append(e)

result = []
for e in p:
    dfs(e,e[0],0)

for e in sorted(result):
    print(e)