# 기하가 너무 좋아
# Gold 4, geometry, bruteforcing

n,m = map(int,input().split())

p = []
for i in range(n+1):
    for j in range(m+1):
        p.append((i,j))
l = len(p)

result = set()
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            x1,y1,x2,y2,x3,y3 = *p[i],*p[j],*p[k]
            if x1 == x2 == x3 or y1 == y2 == y3 or (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2): continue
            a,b,c = (x1-x2)**2+(y1-y2)**2,(x2-x3)**2+(y2-y3)**2,(x3-x1)**2+(y3-y1)**2
            result.add(tuple(sorted((a,b,c))))
print(len(result))