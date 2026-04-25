# 볼록 껍질
# Platinum 5, convex hull

import sys
input = sys.stdin.readline

class Point:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __lt__(self,other):
        return self.x < other.x if self.x != other.x else self.y < other.y
    def incl(self,other):
        return sys.maxsize if self.x == other.x else (self.y-other.y)/(self.x-other.x),self.x,self.y
    def cross(self,other):
        return self.x*other.y-self.y*other.x

def CCW(p,a,b):
    return (a-p).cross(b-p)

def convexHull(arr):
    p = min(arr)
    idx = arr.index(p)
    arr[0],arr[idx] = arr[idx],arr[0]
    arr = arr[:1]+sorted(arr[1:],key=lambda a:a.incl(p))
    hull = []
    for po in arr:
        while len(hull) >= 2 and CCW(hull[-2],hull[-1],po) <= 0:
            hull.pop()
        hull.append(po)
    return hull

arr = [Point(*map(int,input().split())) for _ in range(int(input()))]
print(len(convexHull(arr)))