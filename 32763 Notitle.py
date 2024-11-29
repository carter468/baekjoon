# No title
# Gold 5, ad hoc

import sys
input = sys.stdin.readline

N = int(input())

arr = [0,1]
a = [1]
b = []
for i in range(1,N):
    print(f'? {i} * {i+1}')
    sys.stdout.flush()
    if input().strip() == '+': arr.append(arr[-1])
    else: arr.append(1-arr[-1])
    if arr[-1] == 1: a.append(i+1)
    else: b.append(i+1)

rev = False
if len(a) >= 2:
    print(f'? {a[0]} + {a[1]}')
    sys.stdout.flush()
    if input().strip() == '-': rev = True
else:
    print(f'? {b[0]} + {b[1]}')
    sys.stdout.flush()
    if input().strip() == '+': rev = True

if rev: D = '+-'
else: D = '-+'

print('!',end=' ')
for i in range(1,N+1):
    print(D[arr[i]],end=' ')
sys.stdout.flush()