# 루미상관 수
# Gold 5, bruteforcing

def check(x):
    x = str(x)
    if len(x) == 1: return True
    n = len(x)//2
    return x[:n] == x[-n:]

for _ in range(int(input())):
    N = input()
    l = len(N)
    N = int(N)
    result = set()
    for k in (l-1,l):
        d = k//2
        if d == 0:
            for i in range(1,10):
                j = N-i
                if j > 0 and check(j):
                    result.add((i,j))
                    result.add((j,i))
        else:
            for i in range(10**(d-1),10**d):
                if k%2 == 0:
                    x = int(str(i)*2)
                    j = N-x
                    if x < N and j > 0 and check(j):
                        result.add((x,j))
                        result.add((j,x))
                else:
                    for e in range(10):
                        x = int(str(i)+str(e)+str(i))
                        j = N-x
                        if x < N and j > 0 and check(j):
                            result.add((x,j))
                            result.add((j,x))

    print(len(result))