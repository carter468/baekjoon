# PPAP
# Gold 4, stack

stack = []
for c in input():
    stack.append(c)
    if stack[-4:] == ['P','P','A','P']:
        for _ in range(3):
            stack.pop()
print('PPAP' if stack == ['P'] else 'NP')
