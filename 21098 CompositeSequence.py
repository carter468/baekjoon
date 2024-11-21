# Composite Sequence
# Gold 4, number theory, case work

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0: return False
    return True

n = int(input())
arr = tuple(map(int,input().split()))

if n == 1:
    x = arr[0]
    if isPrime(x): print('No')
    else: print('Yes')
else:
    odd = 0
    one = 0
    for a in arr:
        if a%2: odd += 1
        if a == 1: one += 1
    if odd >= 2:
        if (odd,one) in ((2,2),(3,3)): print('No')
        else: print('Yes')
    elif odd == 0: print('Yes')
    else:
        if n > 2: print('Yes')
        else:
            if arr[0]%2: x = arr[1]
            else: x = arr[0]
            if x != 2: print('Yes')
            else:
                if isPrime(arr[0]) and isPrime(arr[1]) and isPrime(sum(arr)): print('No')
                else: print('Yes')