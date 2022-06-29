# 쿼드트리
import sys
input = sys.stdin.readline

def check(x,y,size):
    one = zero = True
    for i in range(x,x+size):       # 모두 0또는 1인지 확인
        for j in range(y,y+size):
            if video[i][j] == '0':
                one = False
            else:
                zero = False
    if one == True:         
        print('1',end='')
    elif zero == True:
        print('0',end='')
    else:                   # 4분할
        print('(',end='')
        check(x,y,size//2)
        check(x,y+size//2,size//2)
        check(x+size//2,y,size//2)
        check(x+size//2,y+size//2,size//2)
        print(')',end='')

# n = 8
# video = ['11110000','11110000','00011100','00011100',
# '11110000','11110000','11110011','11110011']
n = int(input())
video = []
for _ in range(n):
    video.append(input())
check(0,0,n)
