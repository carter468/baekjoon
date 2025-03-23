# 往復すごろく (Round Sugoroku)
# Gold 4, simulation, implementation

N,A = map(int,input().split())
arr = input()

x = A-1
left,right = [],[]
for i in range(x):
    if arr[i] == '#': left.append(i)
for i in range(x,N):
    if arr[i] == '#': right.append(i)
right = right[::-1]

result = 0
d = 1
while left or right:
    if d == 1:
        if right: nx = right.pop()
        else: nx = N
    else:
        if left: nx = left.pop()
        else: nx = -1
    result += abs(nx-x)
    x = nx
    d *= -1
print(result)