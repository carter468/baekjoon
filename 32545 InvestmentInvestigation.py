# Investment Investigation
# Platinum 4, fenwick tree, priority queue, coordinate compression, simulation

import sys,heapq
input = sys.stdin.readline

def update(i,dif,tree):
    while i <= n:
        tree[i] += dif
        i += (i&-i)

def prefix_sum(i,tree):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

N = int(input())
order = [input().split() for _ in range(N)]

s = set()
for _,_,p,_ in order:
    s.add(int(p))
dic = dict()
for i,a in enumerate(sorted(s)):
    dic[a] = i+1
n = len(dic)

selltree = [0]*(n+1)
buytree = [0]*(n+1)
sellheap = [] # (가격,주문번호,수량) 가장 낮은 가격부터
buyheap = [] # (-가격,주문번호,수량) 가장 높은 가격부터
done = []
for i in range(N):
    a,b,c,d = order[i]
    c,d = int(c),int(d)
    if b == 'normal':
        if a == 'buy': # 일반 매수
            while True:
                if not sellheap or sellheap[0][0] > c: # 거래불가
                    heapq.heappush(buyheap,(-c,i,d))
                    update(dic[c],d,buytree)
                    break
                else: # 거래성사
                    x,y,z = heapq.heappop(sellheap)
                    done.append((y+1,i+1,min(z,d)))
                    update(dic[x],-min(z,d),selltree)
                    if z > d:
                        heapq.heappush(sellheap,(x,y,z-d))
                        break
                    elif z < d:
                        d -= z
                    elif z == d:
                        break
        elif a == 'sell': # 일반 매도
            while True: 
                if not buyheap or -buyheap[0][0] < c: # 거래불가
                    heapq.heappush(sellheap,(c,i,d))
                    update(dic[c],d,selltree)
                    break
                else: # 거래성사
                    x,y,z = heapq.heappop(buyheap)
                    done.append((i+1,y+1,min(z,d)))
                    update(dic[-x],-min(z,d),buytree)
                    if z > d:
                        heapq.heappush(buyheap,(x,y,z-d))
                        break
                    elif z < d:
                        d -= z
                    elif z == d:
                        break
    elif b == 'fok':
        if a == 'buy': # fok매수
            # c이하의 매도수량이 d이상이어야 주문체결.
            if prefix_sum(dic[c],selltree) >= d:
                while d > 0:
                    x,y,z = heapq.heappop(sellheap)
                    if z > d:
                        heapq.heappush(sellheap,(x,y,z-d))
                    done.append((y+1,i+1,min(d,z)))
                    update(dic[x],-min(d,z),selltree)
                    d -= z
        elif a == 'sell': # fok 매도
            # c이상의 매수수량이 d이상이어야 주문체결.
            if prefix_sum(n,buytree)-prefix_sum(dic[c]-1,buytree) >= d:
                while d > 0:
                    x,y,z = heapq.heappop(buyheap)
                    if z > d:
                        heapq.heappush(buyheap,(x,y,z-d))
                    done.append((i+1,y+1,min(d,z)))
                    update(dic[-x],-min(d,z),buytree)
                    d -= z

print(len(done))
for d in done:
    print(*d)