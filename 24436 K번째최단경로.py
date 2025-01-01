# K번째 최단 경로
# Gold 1, combinatorics

def calc(a,b,c,d):
    a,b,c,d = abs(a),abs(b),abs(c),abs(d)
    e = a+b+c+d
    x = 1
    for i in range(2,e+1):
        x *= i
    for i in (a,b,c,d):
        for j in range(1,i+1):
            x //= j
    return x

arr = [[[[0]*10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                arr[a][b][c][d] = calc(a,b,c,d)

for _ in range(int(input())):
    L,k,x,y = input().split()
    L,k = int(L),int(k)

    result = [x]
    x,y = list(map(int,x)),list(map(int,y))
    di = [0]*4
    for i in range(L):
        di[i] = x[i]-y[i]

    if calc(*di) < k:
        print('NO')
        continue

    while k:
        temp = []
        for i in range(L):
            if di[i] < 0: 
                di[i] += 1
                x[i] += 1
                temp.append([''.join(map(str,x)),*di,calc(*di)])
                di[i] -= 1
                x[i] -= 1
            elif di[i] > 0: 
                di[i] -= 1
                x[i] -= 1
                temp.append([''.join(map(str,x)),*di,calc(*di)])
                di[i] += 1
                x[i] += 1
        for s,a,b,c,d,p in sorted(temp):
            if p >= k: 
                result.append(s)
                di = [a,b,c,d]
                x = list(map(int,s))
                if a == b == c == d == 0: k = 0
                break
            k -= p
    print(*result)