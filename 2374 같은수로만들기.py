# 같은 수로 만들기
# Gold 4, stack, greedy

stack = []
result = 0
for _ in range(int(input())):
    x = int(input())
    if stack and x == stack[-1]: continue
    stack.append(x)

    while len(stack) >= 3 and stack[-2] < stack[-3] and stack[-2] < stack[-1]:
        c,b,a = stack.pop(),stack.pop(),stack[-1]
        if a == c:
            result += a-b
        elif a > c:
            result += c-b
            stack.append(c)
        else:
            result += a-b
            stack.append(c)

while len(stack) > 1:
    result += abs(stack.pop()-stack[-1])

print(result)