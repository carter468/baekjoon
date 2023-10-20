# 맹독 방벽
# Platinum 4, convex hull

import sys,math
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
    def length(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

def CCW(p,a,b):
    return (a-p).cross(b-p)
    
n,l = map(int,input().split())
arr = [Point(*map(int,input().split())) for _ in range(n)]

p = min(arr)
idx = arr.index(p)
arr[0],arr[idx] = arr[idx],arr[0]
arr = arr[:1]+sorted(arr[1:],key=lambda x:x.incl(p))

hull = []
for po in arr:
    while len(hull) >= 2 and CCW(hull[-2],hull[-1],po) <= 0:
        hull.pop()
    hull.append(po)

result = l*2*math.pi
for i in range(len(hull)):
    result += hull[i].length(hull[i-1])
print(round(result))