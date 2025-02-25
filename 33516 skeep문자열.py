# skeep 문자열
# Gold 3, stack

def check():
    for i in range(5):
        s = stack[-5+i]
        if i == 0 and s != 's': return False
        if s != '?' and s != 'skeep'[i]: return False
    return True

input()
stack = []
count = 0
for a in input():
    stack.append(a)
    while len(stack) >= 5:
        if check():
            for _ in range(5):
                stack.pop()
            stack.append('?')
            count += 1
        else: break
print(count)