# Black and white stones
# Gold 3, greedy

A,B = map(int,input().split())
S = input()

b,w = [],[]
for i,s in enumerate(S):
    if s == 'B': b.append(i)
    else: w.append(i)
w.reverse()

B = A-B
t = sum(b)
n = len(b)
n = n*(n-1)//2
m = (t-n)*B
c = 0
while w and b:
    i,j = b.pop(),w.pop()
    c += 1
    t -= i-j
    m = min(m,c*A+(t-n)*B)
print(m)