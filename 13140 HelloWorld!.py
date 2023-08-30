# Hello World!
# Gold 5, bruteforce

def solve():
    n = int(input())

    arr = [0]*10
    for h in range(1,10):
        arr[h] = 1
        for w in range(1,10):
            if arr[w] == 0:
                arr[w] = 1
                for e in range(10):
                    if arr[e] == 0:
                        arr[e] = 1
                        for o in range(10):
                            if arr[o] == 0:
                                arr[o] = 1
                                for l in range(10):
                                    if arr[l] == 0:
                                        arr[l] = 1
                                        for r in range(10):
                                            if arr[r] == 0:
                                                arr[r] = 1
                                                for d in range(10):
                                                    if arr[d] == 0:
                                                        x = 10000*h+1000*e+110*l+o
                                                        y = 10000*w+1000*o+100*r+10*l+d
                                                        if x+y == n:
                                                            print(' ',x)
                                                            print('+',y)
                                                            print('-------')
                                                            if n >= 100000: print('',n)
                                                            else: print(' ',n)
                                                            return
                                                arr[r] = 0
                                        arr[l] = 0
                                arr[o] = 0
                        arr[e] = 0
                arr[w] = 0
        arr[h] = 0
    print('No Answer')

solve()