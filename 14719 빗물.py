# 빗물
# Gold 5, implementation

h,w = map(int,input().split())
arr = tuple(map(int,input().split()))

print(sum([max(0,min(max(arr[:i]),max(arr[i+1:]))-arr[i]) for i in range(1,w-1)]))