# 볼링 점수 계산
# Gold 3, implementation

s = input()

score = 0
i = 0
f = 1
p1,p2 = 0,0

while f <= 10:
    a = s[i]
    if a == '-': a = 0
    if a == 'S':
        if p2 == 'S':
            if p1 == 'S': score += 30
            else: score += 20
            p1,p2 = 'S','S'
        else:
            if p2 == 'P':
                score += 10
            score += 10
            p1,p2 = 0,'S'
    else:
        i += 1
        b = s[i]
        if b == '-': b = 0
        if b == 'P':
            if p2 == 'S':
                if p1 == 'S':
                    score += 20+int(a)
                else:
                    score += 20
            elif p2 == 'P':
                score += 10+int(a)
            else:
                score += 10
            p1,p2 = 0,'P'
        else:
            if p2 == 'S':
                if p1 == 'S':
                    score += int(a)*3+int(b)*2
                else:
                    score += int(a)*2+int(b)*2
            elif p2 == 'P':
                score += int(a)*2+int(b)
            else:
                score += int(a)+int(b)
            p1,p2 = 0,0
    i += 1
    f += 1
while i < len(s):
    a = s[i]
    if a == '-': a = 0
    elif a == 'S': a = 10
    elif a == 'P': a = 10-int(s[i-1])
    else: a = int(a)
    score += a
    if (p1,p2) == ('S','S'):
        score += a
        p1,p2 = 0,0
    i += 1
print(score)