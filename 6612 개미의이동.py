# 개미의 이동
# Gold 1, ad hoc

import sys
input = sys.stdin.readline

while True:
    try:
        L,A = map(int,input().split())
    except:
        break

    arr = []
    ml,mr = -1,-1
    l = -1
    for _ in range(A):
        x,d = input().split()
        x = int(x)
        if d == 'L':
            ml = max(x,ml)
            l += 1
        else:
            mr = max(mr,L-x)
        arr.append(x)
    arr.sort()

    if ml == mr:
        t = f'{arr[l]} and {arr[l+1]}'
    elif ml > mr:
        t = f'{arr[l]}'
    else:
        t = f'{arr[l+1]}'
    
    print(f'The last ant will fall down in {max(ml,mr)} seconds - started at {t}.')