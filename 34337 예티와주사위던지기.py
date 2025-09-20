# 예티와 주사위 던지기
# Gold 5, bruteforcing, bitmask

def score(arr):
    m = 0
    for i in range(1,7):
        c = arr.count(i)
        if c == 5: return 50
        m = max(m,i*c)
    return m

Y = tuple(map(int,input().split()))

count = [[0,0] for _ in range(1<<5)]
for i in range(6**5):
    a,b = divmod(i,1296)
    b,c = divmod(b,216)
    c,d = divmod(c,36)
    d,e = divmod(d,6)
    
    arr = [a+1,b+1,c+1,d+1,e+1]
    c = 0
    for i in range(5):
        if Y[i] != arr[i]:
            c += 1<<i
    
    x = score(arr)
    for i in range(1<<5):
        for j in range(5):
            if c>>j&1 and i>>j&1 == 0: break
        else:
            count[i][0] += x
            count[i][1] += 1

m = 0
for a,b in count:
    m = max(m,6**5*a//b)
print(m)