# Nested Dolls
# Platinum 5, LIS

from bisect import bisect_right
 
for _ in range(int(input())):
    N = int(input())
    arr = tuple(map(int,input().split()))
 
    lis = []
    for _,h in sorted([(arr[i*2],arr[i*2+1]) for i in range(N)],key=lambda x:(x[0],-x[1])):
        h = -h
        idx = bisect_right(lis,h)
        if idx == len(lis):
            lis.append(h)
        else:
            lis[idx] = h
    print(len(lis))