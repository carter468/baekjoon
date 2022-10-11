# 숫자 카드 놀이

t = int(input())
for _ in range(t):
    s = sorted(list(input().replace('6','9')))
    num = ['','']
    while len(s) >= 2:
        num[0] += s.pop()
        num[1] += s.pop()
        if num[0] != num[1]:
            break
    while len(s) >= 2:
        num[1] += s.pop()
        num[0] += s.pop()        
    if s:
        num[1] += s.pop()
    print(int(num[0])*int(num[1]))