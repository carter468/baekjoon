# 두 용액

N = int(input())
value_solution = list(map(int,input().split()))
value_solution.sort()

left = 0
right = N-1
mix = value_solution[left] + value_solution[right]
ans = [left,right]

while left<right:
    tmp = value_solution[left] + value_solution[right]
    if abs(tmp) < abs(mix):
        mix = tmp
        ans = [left,right]
        if mix == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(value_solution[ans[0]],value_solution[ans[1]])