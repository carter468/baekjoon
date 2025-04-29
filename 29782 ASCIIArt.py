# ASCII Art
# Gold 5, binary search

def check(x):
    return x*(x+1)//2*26 >= N

for t in range(int(input())):
    N = int(input())

    lo,hi = 0,N
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid
    print(f'Case #{t+1}: {chr((N-lo*(lo+1)//2*26-1)//hi+65)}')