# HTML 에디터
# Gold 1, stack, parsing

def f(a):
    return '<'+a+'>'

while True:
    s = input()

    i = 0
    while s[i] != ' ':
        i += 1
    a = int(s[:i])
    if a == -1: break

    j = i+1
    while s[j] != ' ':
        j += 1
    b = int(s[i:j])

    s = s[j+1:]

    stack = []
    i = 0
    while i < a:
        if s[i] == '<':
            j = i+1
            while s[j] != '>':
                j += 1
            if s[i+1] == '/':
                stack.pop()
            else:
                stack.append(s[i+1:j])
            i = j
        i += 1

    result = list(map(f,stack))
    while i < b:
        if s[i] != '<':
            result.append(s[i])
        else:
            j = i+1
            while s[j] != '>':
                j += 1
            a = s[i+1:j]
            if a[0] == '/':
                stack.pop()
            else:
                stack.append(a)
            result.append(f(a))
            i = j
        i += 1

    while stack:
        result.append(f('/'+stack.pop()))
    print(''.join(result))