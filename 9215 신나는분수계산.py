# 신나는 분수 계산

import sys
input = sys.stdin.readline

def gcd(a,b):   # 최대공약수
    while b!=0:
        a,b = b,a%b
    return a

def add(w,n,d): 
    a = total[1]*d+total[2]*n
    b = total[2]*d
    g = gcd(a,b)
    a //= g
    b //= g
    total[0] += a//b + w
    total[1] = a%b
    total[2] = b
    
test_num = 1
while True:
    n = int(input())
    if n==0:
        break
    total = [0,0,1] # 정수,분자,분모
    for _ in range(n):
        a = input()
        # 3가지 입력형식
        if ',' in a:    # w,n/d
            b,c = map(str,a.split(','))
            w = int(b)
            n,d = map(int,c.split('/'))
        else:
            if '/' in a:    # n/d
                w = 0
                n,d = map(int,a.split('/'))
            else:   # w
                w = int(a)
                n,d = 0,1
        add(w,n,d)

    # 출력    
    if total[0] and total[1]:
        print(f'Test {test_num}: {total[0]},{total[1]}/{total[2]}')
    elif total[0]:
        print(f'Test {test_num}: {total[0]}')
    elif total[1]:
        print(f'Test {test_num}: {total[1]}/{total[2]}')
    else:
        print(f'Test {test_num}: 0')
    test_num += 1