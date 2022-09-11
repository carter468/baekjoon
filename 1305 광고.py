# 광고

L = int(input())
s = input()
n = len(s)

p = [0]*n
i = 0
for j in range(1,n):
    while i>0 and s[i] != s[j]:
        i = p[i-1]
    if s[i] == s[j]:
        i += 1
        p[j] = i

print(n-p[-1])