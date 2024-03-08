# Censoring
# Gold 4, stack

s,t = input(),list(input())

l = len(t)
stack = []
for c in s:
    stack.append(c)
    if len(stack) >= l and stack[-l:] == t:
        for _ in range(l): stack.pop()
print(''.join(stack))