# 다항 함수의 적분
# Gold 5, case work, parsing

def change(x):
    if x == 1: return ''
    if x == -1: return '-'
    return x

s = input()

if s == '0':
    print('W')
elif 'x' in s:
    if s[-1] == 'x':
        print(f'{change(int(s[:-1])//2)}xx+W')
    else:
        a,b = map(int,s.split('x'))
        if b > 0: print(f'{change(a//2)}xx+{change(b)}x+W')
        else: print(f'{change(a//2)}xx{change(b)}x+W')
else:
    print(f'{change(int(s))}x+W')
