# XOR 합 3
# Gold 1, bitmask

N = int(input())
A = tuple(map(int,input().split()))

result = 0
for i in range(30):
    count = 0
    c = 0
    for j in range(N):
        if A[j]>>(29-i)&1:
            c = j-c+1
        count += c
    result += count*1<<(29-i)
print(result)