# 사과나무
# Gold 5, greedy

input()
arr = tuple(map(int,input().split()))

a = sum(arr)
if a%3 == 0: print('YES' if sum([i//2 for i in arr]) >= a//3 else 'NO')
else: print('NO')