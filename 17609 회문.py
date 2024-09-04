# 회문
# Gold 5, case work, string

for _ in range(int(input())):
    s = input()

    if len(s) == 4:
        if s[0] == s[-1]:
            if s[1] == s[-2]: print(0)
            else: print(1)
        else:
            if s[1] == s[-1] or s[0] == s[-2]: print(1)
            else: print(2)
        continue

    a,b,c = True,True,True
    f = False
    for i in range(len(s)//2+1):
        if f:
            if s[i+1] != s[-1-i]: b = False
            if s[i] != s[-2-i]: c = False
        if s[i] != s[-1-i]:
            a = False
            f = True
    if a: print(0)
    elif b or c: print(1)
    else: print(2)
