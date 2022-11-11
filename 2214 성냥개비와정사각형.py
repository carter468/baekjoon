# 2214 성냥개비와 정사각형
# Gold 3, 문자열

import sys
input = sys.stdin.readline

def check_square(i,j,k):
    # 왼쪽 오른쪽변
    for l in range(k):
        if '*' in [array[i+l*2+1][j],array[i+l*2+1][j+k]]:
            return False
    # 밑변
    if '*' in array[i+2*k][j:j+k]:
        return False
    return True

while True:
    r,c = map(int,input().split())
    if r==0 and c==0:
        break
    array = []
    for _ in range(r*2+1):
        array.append(input().strip())
        
    count = 0
    for i in range(0,r*2+1,2):  # 열
        for j in range(c):      # 행
            for k in range(1,c-j+1):  # 한변의길이
                # 윗변의 가로 모양, 세로 길이가 조건에 맞으면 체크
                if '*' not in array[i][j:j+k] and i+k*2<=r*2:
                    if check_square(i,j,k):
                        count += 1
    
    print(count,'squares')