# 배열 나누기
# Gold 3, greedy, stack

input()

stack = []
for a in map(int,input().split()):
    if a < 0:
        while stack:
            a += stack.pop()
            if a >= 0:
                stack.append(a)
                break
        else: exit(print(-1))
    else:
        stack.append(a)
print(len(stack))