# 바둑이 포커
# Gold 5, implementation

from functools import cmp_to_key

num = {}
for i,a in enumerate('123456789abcdef'):
    num[a] = i

def cmp(a,b):
    def rank(x):
        arr = []

        n1,n2 = num[x[0]],num[x[2]]
        c1,c2 = x[1],x[3]

        if abs(n1-n2) in (1,14): arr.append(1)
        elif n1 == n2: arr.append(2)
        else: arr.append(3)

        if c1 == c2: arr.append(1)
        else: arr.append(2)

        arr.append(-max(n1,n2))
        arr.append(-min(n1,n2))

        if n1 < n2:
            if c2 == 'b': arr.append(1)
            else: arr.append(2)
        elif n1 > n2:
            if c1 == 'b': arr.append(1)
            else: arr.append(2)
        else:
            arr.append(1)

        return arr

    ra = rank(a)
    rb = rank(b)
    for i in range(5):
        if ra[i] > rb[i]: return 1
        elif ra[i] < rb[i]: return -1

card = input().split(',')

pair = []
for i in range(6):
    for j in range(i+1,6):
        pair.append(card[i]+card[j])

print(*sorted(pair,key=cmp_to_key(cmp)),sep='\n')