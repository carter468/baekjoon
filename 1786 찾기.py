# 찾기 

# KMP 알고리즘

t = input()
p = input()

n = len(p)
m = len(t)
pi = [0]*n
i = 0
for j in range(1,n):
    while i>0 and p[i] != p[j]:
        i = pi[i-1]
    if p[i] == p[j]:
        i += 1
        pi[j] = i

cnt = 0
ans = []
i = 0
for j in range(0,m):
    while i>0 and p[i] != t[j]:
        i = pi[i-1]
    if p[i] == t[j]:
        i += 1
        if i == n:
            ans.append(j-i+2)
            cnt += 1
            i = pi[i-1]
print(cnt)
print(*ans)