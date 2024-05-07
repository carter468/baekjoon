# 모든 스택 수열
# Gold 5, backtracking

def solve(stack,arr,idx):
    if idx == n:
        result.append(arr+stack[::-1])
        return
    if stack:
        arr1 = arr+[stack[-1]]
        stack1 = stack[:-1]
        solve(stack1,arr1,idx)
    solve(stack+[idx+1],arr,idx+1)

n = int(input())
result = []
solve([],[],0)
for r in result:
    print(*r)