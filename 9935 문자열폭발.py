# 문자열 폭발

string = input()
bomb = input()
length_bomb = len(bomb)
lastchar = bomb[-1]
stack = []
for s in string:
    stack.append(s)
    if lastchar == s and stack[-length_bomb:] == list(bomb):
        del stack[-length_bomb:]
if stack:
    print(''.join(stack))
else:
    print('FRULA')