# 호연이와 파이썬
# Gold 3, eulerian path

N = int(input())
if N%2 == 1:
    print(N*(N-1)//2)
else:
    print(N*(N-1)//2+(N//2)-1)