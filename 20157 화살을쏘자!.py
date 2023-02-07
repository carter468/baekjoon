# 화살을 쏘자!
# Gold 5, 기하학, 자료구조

from collections import defaultdict
import sys
input = sys.stdin.readline

def add(i,j):
    if j>0:
        ballons['+'+str(i)] += 1
    else:
        ballons['-'+str(i)] += 1
            
ballons = defaultdict(int)   # 기울기, 방향
for _ in range(int(input())):
    x,y = map(int,input().split())
    if y==0:
        add('x',x)
    elif x==0:
        add('y',y)
    else:
        add(y/x,y)
        
print(max(ballons.values()))

# import sys
# input = sys.stdin.readline

# def count(i,j):
#     if i in ballons:
#         if j>0:
#             ballons[i][0] += 1
#         else:
#             ballons[i][1] += 1
#     else:
#         if j>0:
#             ballons[i] = [1,0]
#         else:
#             ballons[i] = [0,1]
            
# ballons = {}    # 기울기, 방향
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     if y==0:
#         count('x',x)
#     elif x==0:
#         count('y',y)
#     else:
#         count(y/x,y)
        
# result = 0
# for a in ballons:
#     result = max(result,(max(ballons[a])))
# print(result)
