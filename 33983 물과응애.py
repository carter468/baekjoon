# 물과 응애
# Gold 5, ad hoc

input()
S = input()

c = S.count('O')
if len(S)-c != c*2: exit(print('mix'))

a,b = 0,0
for s in S:
    if s == 'H':
        if c:
            a += 1
            c -= 1
        else:
            if b:
                b -= 1
            else:
                exit(print('mix'))
    else:
        if a:
            a -= 1
            b += 1
        else:
            exit(print('mix'))
print('pure')