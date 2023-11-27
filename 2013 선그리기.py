# 선 그리기
# Gold 2, line intersection, disjoint set

# 5964ms
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class Point:
    def __init__(self,x,y):
        self.x,self.y = int(round(x*100)),int(round(y*100))
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __le__(self,other):
        return self.x < other.x if self.x != other.x else self.y <= other.y
    def cross(self,other):
        return self.x*other.y-self.y*other.x

def CCW(a,b,p):
    return (a-p).cross(b-p)

n = int(input())
arr = [tuple(map(float,input().split())) for _ in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = list(range(n))
for i in range(n):
    x1,y1,x2,y2 = arr[i]
    A,B = Point(x1,y1),Point(x2,y2)
    if B <= A: A,B = B,A
    for j in range(i+1,n):
        x3,y3,x4,y4 = arr[j]
        C,D = Point(x3,y3),Point(x4,y4)
        if D <= C: C,D = D,C
        if (CCW(A,B,C),CCW(A,B,D)) == (0,0) and C <= B and A <= D:
            parent[find(j)] = find(i)

result = 0
for i in range(n):
    if find(i) == i: result += 1
print(result)

# 2740ms
# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# class Point:
#     def __init__(self,x,y):
#         self.x,self.y = x,y
#     def __sub__(self,other):
#         return Point(self.x-other.x,self.y-other.y)
#     def cross(self,other):
#         return self.x*other.y-self.y*other.x

# def CCW(a,b,p):
#     return (a-p).cross(b-p)

# def ge(a,b):
#     if a.x > b.x: return 1
#     elif a.x < b.x: return 0
#     elif a.y >= b.y: return 1
#     else: return 0

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# n = int(input())
# arr = []
# for _ in range(n):
#     a,b,c,d = map(lambda x:int(round(float(x)*100)),input().split())
#     arr.append((a,b,c,d))

# parent = list(range(n))
# for i in range(n):
#     x1,y1,x2,y2 = arr[i]
#     for j in range(i+1,n):
#         x3,y3,x4,y4 = arr[j]
#         A,B,C,D = Point(x1,y1),Point(x2,y2),Point(x3,y3),Point(x4,y4)
#         if ge(A,B): A,B = B,A
#         if ge(C,D): C,D = D,C
#         if (CCW(A,B,C),CCW(A,B,D)) == (0,0):
#             if ge(A,C): A,B,C,D = C,D,A,B
#             if ge(B,C) or (B.x,B.y) == (C.x,C.y):
#                 parent[find(j)] = find(i)

# for i in range(n):
#     find(i)
# print(len(set(parent)))