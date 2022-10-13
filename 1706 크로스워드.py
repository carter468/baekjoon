# 크로스워드

r,c = map(int,input().split())
puzzle = []
for _ in range(r):
    puzzle.append(list(input()))
word = []
for i in range(r):
    tmp = ''
    for x in puzzle[i]:
        if x != '#':
            tmp += x
        elif len(tmp) > 1:
            word.append(tmp)
            tmp = ''
        else:
            tmp = ''
    if len(tmp) > 1:
        word.append(tmp)
for i in range(c):
    tmp = ''
    for j in range(r):
        if puzzle[j][i] != '#':
            tmp += puzzle[j][i]
        elif len(tmp) > 1:
            word.append(tmp)
            tmp = ''
        else:
            tmp = ''
    if len(tmp) > 1:
        word.append(tmp)
word.sort()
print(word[0])