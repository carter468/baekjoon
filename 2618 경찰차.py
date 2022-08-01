# 경찰차

from cgi import print_arguments


n = int(input())
w = int(input())

incident = []
for _ in range(w):
    incident.append(list(map(int,input().split())))

print(incident)
