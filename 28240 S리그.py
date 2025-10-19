# S리그
# Gold 2, constructive, ad hoc

def fill(s,e,dx,dy):
    x,y = result[s]
    i = s
    while (i+1)%N != e:
        i = (i+1)%N
        x += dx
        y += dy
        result[i] = x,y

MAX = 9999
N = int(input())
a,b,c,d = map(int,input().split())
a,b,c,d = a-1,b-1,c-1,d-1

if a > b: a,b = b,a
if c > d: c,d = d,c
if a > c: a,b,c,d = c,d,a,b

result = [0]*N
if c < b:
    result[b] = 0,0
    result[c] = -MAX,-MAX
    result[d] = MAX,-MAX
    result[a] = 0,MAX
    if b < d:
        fill(b,d,1,-1)
        fill(d,a,-1,2)
        fill(a,c,-1,-2)
        fill(c,b,1,1)
    else:
        result[b] = MAX,0
        fill(a,c,-1,-1)
        fill(c,d,1,1)
        fill(d,b,0,1)
        fill(b,a,0,1)
else:
    result[b] = 0,0
    result[c] = MAX,0
    result[a] = 1,MAX
    result[d] = MAX-1,MAX
    fill(b,c,1,0)
    fill(c,d,0,1)
    fill(d,a,-1,0)
    fill(a,b,0,-1)

for r in result: print(*r)