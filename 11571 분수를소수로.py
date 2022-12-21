# 분수를 소수로
# Gold 5, 수학

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    m = [0]*b
    idx = 2
    temp = str(a//b)
    m[a%b] = 1
    a = (a%b)*10
    answer = ''
    while True:
        answer += str(a//b)
        c = a%b
        if m[c]:
            break
        m[c] = idx
        idx += 1
        a = c*10
    print(temp+'.'+answer[:m[c]-1]+'('+answer[m[c]-1:]+')')