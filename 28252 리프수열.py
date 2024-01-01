# 리프 수열
# Gold 2, constructive

input()
arr = list(map(int,input().split()))

graph = [[] for _ in range(100001)]
x = arr.pop()
if x == 1:
    leaf = [1]
    node = 2
elif x == 2:
    graph[1].append(2)
    leaf = [1,2]
    node = 3
else:
    print(-1)
    exit()

while arr:
    x = arr.pop()
    if x == 1 or x < len(leaf):
        print(-1)
        break
    temp = []
    for i in range(x):
        graph[leaf[i%len(leaf)]].append(node)
        temp.append(node)
        node += 1
    leaf = temp
else:
    print(node-1)
    for i in range(1,node):
        for x in graph[i]:
            print(i,x)