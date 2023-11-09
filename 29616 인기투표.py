# 인기투표
# Gold 5, math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

n,p = map(int,input().split())
prev = list(map(int,input().split()))
now = list(map(int,input().split()))

g = prev[0]
for x in prev:
    g = gcd(g,x)
count_p = 0
for i in range(n):
    prev[i] //= g
    count_p += prev[i]
    
g = now[0]
for x in now:
    g = gcd(g,x)
count_n = 0
for i in range(n):
    now[i] //= g
    count_n += now[i]

c = 1
for i in range(n):
    if now[i] < prev[i]:
        c = max(c,(prev[i]-1)//now[i]+1)
print(count_p,count_n*c)