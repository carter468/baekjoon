# 지민이의 테러
# Platinum 5, 선분교차판정, 다각형 내부의 점 판정
import sys
input = sys.stdin.readline

def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[0]*c[1]-c[0]*b[1]-b[0]*a[1]

def meet(A,B,C,D):
    return ccw(A,B,C)*ccw(A,B,D)<0 and ccw(C,D,A)*ccw(C,D,B)<0

def solve():
    A = tuple(map(int,input().split()))
    B = (10**9+1,A[1]+1)    # 입력된 방어막과 일직선이 될 수 없도록 AB 설정

    # 선분AB와 방어막의 교점의 개수를 구한다
    count = 0
    for i in range(N):
        C,D = shield[i-1],shield[i]
        if ccw(A,C,D)==0:  
            # A가 방어막 위에 있는 경우
            if min(C[0],D[0])<=A[0]<=max(C[0],D[0]) and min(C[1],D[1])<=A[1]<=max(C[1],D[1]):
                return 1
        else:
            count += meet(A,B,C,D)
    
    return count%2  # 교점이 홀수개면 내부의 점

N = int(input())
shield = [tuple(map(int,input().split())) for _ in range(N)]
for _ in range(3):
    print(solve())