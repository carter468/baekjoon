# 돌 뒤집기 게임
# Platinum 5, game theory, ad hoc

input()
S = input()+'T'

n = S.count('H')
result = 'Second'
c = 0
for s in S:
    if s == 'H':
        c += 1
    else:
        if c == 4:
            n -= 1
        elif c > 2:
            result = 'First'
        c = 0
if n%2 == 1: result = 'First'
print(result)