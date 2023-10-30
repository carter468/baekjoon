# 접기 포개기
# Gold 2, stack

def solve(arr):
    stack = []
    for a in arr:
        stack.append(a)
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            b = stack.pop()
            stack.append(b*2)
    return max(stack)

input()
arr = tuple(map(int,input().split()))
print(max(solve(arr),solve(arr[::-1])))