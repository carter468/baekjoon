# 색종이 만들기
import sys
input = sys.stdin.readline

def check(x,y,size):
    global white,blue
    one = zero = True
    for i in range(x,x+size):       #전부 같은 색인지 확인
        for j in range(y,y+size):
            if paper[i][j] == 1:
                zero = False
            else:
                one = False
    if zero == True:
        white += 1
    elif one == True:
        blue += 1
    else:
        check(x,y,size//2)      # 종이를 4등분해서 다시 확인
        check(x+size//2,y,size//2)
        check(x,y+size//2,size//2)
        check(x+size//2,y+size//2,size//2)
n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))
# paper = [[1, 1, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0],[1, 0, 0, 0, 1, 1, 1, 1],[0, 1, 0, 0, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1]]
white = blue = 0
check(0,0,n)
print(white)
print(blue)