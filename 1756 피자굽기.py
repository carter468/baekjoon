# 피자 굽기
# Gold 5, implementation

d,n = map(int,(input().split()))
arr = list(map(int,input().split()))

for i in range(1,d):
    arr[i] = min(arr[i],arr[i-1])
for a in map(int,input().split()):
    while arr and a > arr[-1]:
        arr.pop()
    if arr: arr.pop()
    else: 
        print(0)
        break
else: print(len(arr)+1)
