# 시큼한 표정
# Gold 4, combinatorics

def comb(a,b):
    x = a+b
    r = 1
    for i in range(b):
        r = r*(x-i)//(i+1)
    return r

M = 10**9+7

n = int(input())
s = input()
result = 0
for i in range(n-1):
    l,r = i,i+1
    while 0 <= l and r < n and s[l] == '>' and s[r] == '<':
        result = (result+comb(l,n-r-1))%M
        l,r = l-1,r+1
print(result)
