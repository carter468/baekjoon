# 식물 기르기
# Gold 4, greedy, math

input()
arr = tuple(map(int,input().split()))

m = max(arr)
count = 0
for a in arr:
    count += m//a
print((count-1)//m+1)
