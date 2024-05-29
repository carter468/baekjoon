# Web Pages
# Gold 4, stack, parsing

while (s:=input()) != '#':
    l = len(s)
    stack = []
    i = 0
    while i < l:
        while i < l and s[i] != '<':
            i += 1
        if i < l:
            i += 1
            a = ''
            while s[i] != '>':
                a += s[i]
                i += 1
            b = a.split()
            c,d = b[0],b[-1]
            if c[0] != '/':
                if d != '/':
                    stack.append(c)
            else:
                if stack and stack[-1] == c[1:]:
                    stack.pop()
                else:
                    print('illegal')
                    break
    else: 
        print('illegal' if stack else 'legal')