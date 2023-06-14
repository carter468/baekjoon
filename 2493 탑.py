# 탑
# Gold 5, 스택

n = int(input())

arr = tuple(map(int,input().split()))
tower = []
for i in range(n):
    while tower and tower[-1][0] < arr[i]:
        tower.pop()
    if tower:
        print(tower[-1][1],end=' ')
    else:
        print(0,end=' ')
    tower.append((arr[i],i+1))

# n = int(input())

# arr = tuple(map(int,input().split()))
# tower = [(10**8,0)]
# for i in range(n):
#     while tower[-1][0] < arr[i]:
#         tower.pop()
#     print(tower[-1][1],end=' ')
#     tower.append((arr[i],i+1))