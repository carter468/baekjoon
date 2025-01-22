# Exchange Rates
# Gold 1, DFS

from collections import defaultdict

def f(x,y):
    a,b = x,y
    while b:
        a,b = b,a%b
    return x//a,y//a

dic = defaultdict(dict)
while True:
    query = input().split()
    if query[0] == '.': break
    if query[0] == '?':
        a,_,b = query[1:]
        visited = {a}
        q = [(a,1,1)]
        while q:
            x,y,z = q.pop()
            if x == b:
                print(y,a,'=',z,b)
                break
            for nx in dic[x]:
                if nx not in visited:
                    visited.add(nx)
                    t1,t2 = dic[x][nx]
                    ny,nz = f(y*t1,z*t2)
                    q.append((nx,ny,nz))
        else:
            print('?',a,'= ?',b)
    elif query[0] == '!':
        a,b,_,c,d = query[1:]
        a,c = f(int(a),int(c))
        dic[b][d] = (a,c)
        dic[d][b] = (c,a)