# 솹씨 몇 도예요?
# Gold 5, binary search

import sys
input = sys.stdin.readline

l,r = 0,2025
while True:
    t = (l+r)//2
    print('?',t)
    sys.stdout.flush()
    
    s = input()[0]
    if s == 'S':
        print('!',t)
        break
    elif s == 'H':
        l,r = (l+t)//2,(t-1+t)//2
    else:
        l,r = (t+1+t)//2,(r+t)//2