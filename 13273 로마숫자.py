# 로마 숫자

import sys
input = sys.stdin.readline

rome_to_arabian = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
rome_to_arabian_shorten = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
arabian_to_rome = {b:a for a,b in rome_to_arabian.items()}
arabian_to_rome_shorten = {b:a for a,b in rome_to_arabian_shorten.items()}

def change_arabian(s):
    answer = ''
    for i,a in enumerate(s):
        x = int(a)*10**(len(s)-i-1)
        if x in arabian_to_rome_shorten:
            answer += arabian_to_rome_shorten[x]
        else:
            if int(a) >= 5:
                answer += arabian_to_rome[5*10**(len(s)-i-1)] + arabian_to_rome[10**(len(s)-i-1)]*(int(a)-5)
            else:
                answer += arabian_to_rome[10**(len(s)-i-1)]*int(a)
    print(answer)

def change_rome(s):
    answer = 0
    for x in rome_to_arabian_shorten:
        if x in s:
            answer += rome_to_arabian_shorten[x]
            s = s.replace(x,'')
    for x in s:
        answer += rome_to_arabian[x]
    print(answer)
    
for _ in range(int(input())):
    s = input().strip()
    if s.isdigit():
        change_arabian(s)
    else:
        change_rome(s)