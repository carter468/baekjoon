# Tier and Rank
# Gold 4, implementation

import sys
input = sys.stdin.readline

n,t = map(int,input().split())
tier = []
for _ in range(t):
    a,b = input().split()
    if b[-1] == '%':
        b = int(b[:-1])
        tier.append((a,n*b//100))
        n -= n*b//100
    else:
        b = int(b)
        tier.append((a,min(n,b)))
        n -= min(n,b)
x = input().strip()

if n != 0: print('Invalid System')
else:
    if x[-1].isdigit():
        x,y = x[:-1],int(x[-1])
        rank = 0
        for a,b in tier:
            if a == x:
                z = (b-1)//4+1
                for i in range(y-1):
                    rank += z
                    b -= z
                if b <= 0: print('Liar')
                else: print(rank+1,rank+min(b,z))
                break
            else:
                rank += b
        else:
            print('Liar')
    else:
        rank = 0
        for a,b in tier:
            if a == x:
                if b == 0: print('Liar')
                else: print(rank+1,rank+b)
                break
            else:
                rank += b
        else:
            print('Liar')