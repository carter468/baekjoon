# 경숲길 재개발 1
# Gold 5, divide and conquer

def solve(x):
    if x == 0: return 0
    for i in range(N):
        if x == arr[i]:
            return s[i]
        if x < arr[i]:
            return s[i-1]+i+1+solve(x-1-arr[i-1])

N = int(input())

i = 1
arr = [1]
s = [1]
while arr[-1] <= N:
    i += 1
    arr.append(arr[-1]*2+1)
    s.append(s[-1]*2+i)

print(solve(N))