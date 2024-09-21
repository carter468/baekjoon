# 이진수
# Gold 4, DP

arr = [0,0,1]
for i in range(998):
    if i%2 == 1: arr.append(arr[-1]*2+1)
    else: arr.append(arr[-1]*2-1)

print(arr[int(input())])
