# Cow Line
# Gold 5, combinatorics

import sys
input = sys.stdin.readline

arr = [1]
for i in range(1,21):
    arr.append(arr[-1]*i)

n,k = map(int,input().split())
for _ in range(k):
    if input().strip() == 'P':
        a = int(input())
        num = list(range(1,n+1))
        for i in range(n):
            c,a = divmod(a-1,arr[n-i-1])
            a += 1
            print(num[c],end=' ')
            num.remove(num[c])
        print()
    else:
        a = tuple(map(int,input().split()))
        num = list(range(1,n+1))
        result = 1
        for i in range(n):
            result += arr[n-i-1]*num.index(a[i])
            num.remove(a[i])
        print(result)