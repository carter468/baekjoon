# 경찰차


n = int(input())
w = int(input())

p1 = [1,1]
p2 = [n,n]
for _ in range(w):
    incident = list(map(int,input().split()))
    p1.append(incident)
    p2.append(incident)

dp = [[0]*(w+1) for _ in range(w+1)]
trace = [['']*(w+1) for _ in range(w+1)]

for i in range(w):
    for j in range(w):
        
def dist(a,b):

