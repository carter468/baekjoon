# 순열과 연산
# Platinum 4, ad hoc, case work

n = int(input())
arr = list(map(int,input().split()))

def query2(a,b):
    x,y = min(arr[a],arr[b]),max(arr[a],arr[b])
    temp = [0]*n
    for i in range(n):
        if a <= i <= b:
            if arr[i] > y: temp[i] = x
            elif arr[i] < x: temp[i] = y
            else: temp[i] = arr[i]
        else: temp[i] = arr[i]
    return temp

temp = query2(0,n-1)
if temp[0] == temp[-2]:
    print(3)
    print(2,1,n)
    print(1,n-1)
    print(2,1,n)
    exit()
elif temp[1] == temp[-1]:
    print(3)
    print(2,1,n)
    print(1,1)
    print(2,1,n)
    exit()

arr[0],arr[1] = arr[1],arr[0]
temp = query2(0,n-1)
if temp[0] == temp[-2]:
    print(4)
    print(1,1)
    print(2,1,n)
    print(1,n-1)
    print(2,1,n)
    exit()
elif temp[1] == temp[-1]:
    print(4)
    print(1,1)
    print(2,1,n)
    print(1,1)
    print(2,1,n)
    exit()

arr[0],arr[1] = arr[1],arr[0]
arr[-2],arr[-1] = arr[-1],arr[-2]
temp = query2(0,n-1)
if temp[0] == temp[-2]:
    print(4)
    print(1,n-1)
    print(2,1,n)
    print(1,n-1)
    print(2,1,n)
elif temp[1] == temp[-1]:
    print(4)
    print(1,n-1)
    print(2,1,n)
    print(1,1)
    print(2,1,n)