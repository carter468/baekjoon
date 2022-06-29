# 종이의 개수
import sys
input = sys.stdin.readline

def check(x,y,size):
    num_first = paper[x][y]
    global result_minus , result_zero , result_plus
    for i in range(x,x+size):
        for j in range(y,y+size):
            if paper[i][j] != num_first:    #9분할
                check(x,y,size//3)
                check(x+size//3,y,size//3)
                check(x+size*2//3,y,size//3)
                check(x,y+size//3,size//3)
                check(x,y+size*2//3,size//3)
                check(x+size//3,y+size//3,size//3)
                check(x+size//3,y+size*2//3,size//3)
                check(x+size*2//3,y+size*2//3,size//3)
                check(x+size*2//3,y+size//3,size//3)
                return
    if num_first == -1:
        result_minus += 1
    elif num_first == 0:
        result_zero += 1
    elif num_first == 1:
        result_plus += 1

# n = 9
# paper = [
# [0, 0, 0, 1, 1, 1, -1, -1, -1],
# [0, 0, 0, 1, 1, 1, -1, -1, -1],
# [0, 0, 0, 1, 1, 1, -1, -1, -1],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0, 0, 0, 0],
# [0, 1, -1, 0, 1, -1, 0, 1, -1],
# [0, -1, 1, 0, 1, -1, 0, 1, -1],
# [0, -1, 1, 0, 1, -1, 0, 1, -1]]

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

result_minus = result_zero = result_plus = 0

check(0,0,n)
print(result_minus)
print(result_zero)
print(result_plus)