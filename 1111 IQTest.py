# IQ Test
# Gold 3, math, casework, bruteforcing

n = int(input())
arr = tuple(map(int,input().split()))

if n == 1: print('A')
elif n == 2: print(arr[0] if arr[0] == arr[1] else 'A')
else:
    if arr[0] == arr[1]:
        for i in range(2,n):
            if arr[i] != arr[0]:
                print('B')
                break
        else: print(arr[0])
    elif (arr[2]-arr[1])%(arr[1]-arr[0]) != 0: print('B')
    else:
        a = (arr[2]-arr[1])//(arr[1]-arr[0])
        b = arr[1]-arr[0]*a
        for i in range(3,n):
            if arr[i] != arr[i-1]*a+b:
                print('B')
                break
        else:
            print(arr[-1]*a+b)