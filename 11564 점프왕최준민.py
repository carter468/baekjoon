# 점프왕 최준민

k,a,b = map(int,input().split())

left = a//k
if a%k != 0:
    left += 1
right = b//k
print(right-left+1)