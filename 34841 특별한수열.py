# 특별한 수열
# Gold 2, fenwick tree

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i <= N:
        tree[i] += dif
        i += (i&-i)

def search1(x):
    lo,hi = 0,N+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        if prefix_sum(mid) >= x: hi = mid
        else: lo = mid
    return hi

def search2(x):
    lo,hi = 0,N+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        if prefix_sum(mid) > x: hi = mid
        else: lo = mid
    return hi

N = int(input())
A = tuple(map(int,input().split()))

dic = dict()
dic_r = dict()
for a,i in [(a,i) for i,a in enumerate(sorted(A),1)]:
    dic[i] = a
    dic_r[a] = i

tree = [0]*(N+1)
count = dict()
dif = set()
for i in range(N):
    a = A[i]
    b = dic_r[a]
    
    update(b,1)
    c = prefix_sum(b)
    if c == 1:
        if i != 0:
            x = search2(c)
            d = dic[x]-a
            count[d] = count.get(d,0)+1
            dif.add(d)
    elif c == i+1:
        x = search1(c-1)
        d = a-dic[x]
        count[d] = count.get(d,0)+1
        dif.add(d)
    else:
        x = search1(c-1)
        y = search2(c)
        x,y = dic[x],dic[y]
        d = y-x
        if count.get(d,0) > 0:
            count[d] -= 1
            if count[d] == 0:
                dif.remove(d)
        
        for d in (a-x,y-a):
            count[d] = count.get(d,0)+1
            dif.add(d)
    
    print(1 if len(dif) <= 1 else 0)