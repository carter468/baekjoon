# Shuffles
# Gold 3, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

count = 0
check = [False]*(N+2)
for a in A:
    if not check[a]: count += 1
    check[a+1] = True

result = 0
while 1<<result < count:
    result += 1
print(result)