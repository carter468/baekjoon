# 오름세
# Gold 2, LIS

import bisect

while True:
    try:
        N = int(input())
    except:
        break
    
    lis = [0]
    for x in map(int,input().split()):
        if x > lis[-1]:
            lis.append(x)
        else:
            lis[bisect.bisect_left(lis,x)] = x
    print(len(lis)-1)