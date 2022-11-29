# 13900 순서쌍의 곱의 합
# Silver 4, 수학

input()
nums = tuple(map(int,input().split()))

total = sum(nums)
answer = 0
for n in nums:
    answer += (total-n)*n
print(answer//2)