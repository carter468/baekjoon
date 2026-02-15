# Sequence Merging
# Gold 4, stack, greedy

import sys
input = sys.stdin.readline

for t in range(int(input())):
    input()

    result = 0
    stack = []
    for x in map(int,input().split()):
        stack.append(x)
        while len(stack) >= 3 and stack[-2] < stack[-1]:
            c,b,a = stack.pop(),stack.pop(),stack.pop()
            if max(a,b) < max(b,c):
                result += max(a,b)
                stack.append(max(a,b))
                stack.append(c)
            else:
                result += max(b,c)
                stack.append(a)
                stack.append(max(b,c))
    
    while len(stack) >= 3:
        stack.pop()
        result += stack[-1]
    result += max(stack)
    
    print(f'Case #{t+1}: {result}')