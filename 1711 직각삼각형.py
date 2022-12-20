# 직각삼각형
# Silver 1, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

def get_length_square(a,b):
    return (point[a][0]-point[b][0])**2 + (point[a][1]-point[b][1])**2

point = []
n = int(input())
for _ in range(n):
    point.append(tuple(map(int,input().split())))

answer = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a = get_length_square(i,j)
            b = get_length_square(j,k)
            c = get_length_square(k,i)
            if a+b==c or b+c==a or c+a==b:
                answer += 1
print(answer)