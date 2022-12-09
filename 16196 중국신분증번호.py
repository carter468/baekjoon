# 중국 신분증 번호
# Silver 1, 구현, 문자열

import sys
input = sys.stdin.readline

def checkid():    
    id_num = input().strip()

    # 지역 코드 확인
    for _ in range(int(input())):
        if id_num[:6] == input().strip():
            break
    else:
        return 'I'
    
    # 생일 코드 확인
    y = int(id_num[6:10])
    m = int(id_num[10:12])
    d = int(id_num[12:14])
    if y>2011 or y<1900 or m<1 or m>12 or d<1:
        return 'I'
    if m==2:
        if ((y%4==0 and y%100!=0) or y%400==0):
            if d>29:
                return 'I'
        elif d>28:
            return 'I'
    elif m in [4,6,9,11]:
        if d>30:
            return 'I'
    elif d>31:
        return 'I'

    # 숫자 코드
    num_code = int(id_num[14:17])
    if num_code == 0:
        return 'I'
    
    # 체크섬 코드
    checksum = 0
    for i,a in enumerate(id_num[:17]):
        checksum += int(a)*(2**(17-i))%11
    checksum = (12-checksum%11)%11
    if checksum == 10:
        if id_num[17] != 'X':
            return 'I'
    elif str(checksum) != id_num[17]:
        return 'I'
    
    # 남여
    if num_code%2:
        return 'M'
    else:
        return 'F'

print(checkid())