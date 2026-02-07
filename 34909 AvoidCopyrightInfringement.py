# Avoid Copyright Infringement
# Platinum 5, ad hoc, constructive, case work

for _ in range(int(input())):
    x,y,z = map(int,input().split())

    if x == 0:
        if abs(y-z) > 1:
            print('NO')
            continue
        print('YES')
        if y > z:
            print('IT'*z+'I')
        else:
            print('TI'*y+'T'*(z-y))
        continue
    elif y == 0:
        if abs(x-z) > 1:
            print('NO')
            continue
        print('YES')
        if x > z:
            print('MT'*z+'M')
        else:
            print('TM'*x+'T'*(z-x))
        continue
    elif z == 0:
        if abs(x-y) > 1:
            print('NO')
            continue
        print('YES')
        if x > y:
            print('MI'*y+'M')
        else:
            print('IM'*x+'I'*(y-x))
        continue

    a = max(0,abs(x-z)-1)
    b = x+z
    if a <= y <= b:
        c = b-y
        if c%2 == 0:
            c //= 2
            result = ['M']*(x-c)+['TM']*c+['T']*(z-c)
        else:
            c //= 2
            if x > z:
                result = ['M']*(x-c-1)+['TM']*c+['T']*(z-c)+['M']
            else:
                result = ['T']+['M']*(x-c)+['TM']*c+['T']*(z-c-1)

        for i in range(len(result)-1):
            a = result[i][-1]+result[i+1][0]
            if a == 'MM':
                result[i] += 'I'
                y -= 1
            elif a == 'TT':
                result[i] += 'I'
                y -= 1
        if y:
            result.append('I')
            y -= 1
        if y:
            result[0] = 'I'+result[0]
        print('YES')
        print(''.join(result))
    else: 
        print('NO')