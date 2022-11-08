# 안테나

n = int(input())
array = list(map(int,input().split()))

# 중앙값을 찾는다.
array.sort()
if n%2==0:
    print(array[n//2-1])
else:
    print(array[n//2])