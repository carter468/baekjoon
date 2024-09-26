# 주사위 윷놀이
# Gold 2, implementation, simulation, backtracking

def move(start,d):
    x = start
    for _ in range(d):
        if x in (5,10,15) and x == start: x = graph[x][1]
        else: x = graph[x][0]
    return x

def solve(state,idx,total):
    global result
    result = max(result,total)
    if idx == 10: return
    for i in range(4):
        if state[i] == 32: continue
        x = move(state[i],arr[idx])
        temp = state[i]
        state[i] = 0
        if x == 32 or (x != 32 and x not in state):
            state[i] = x
            solve(state,idx+1,total+score[x])
        state[i] = temp

graph = [[] for _ in range(33)]
for i in range(20): graph[i].append(i+1)
graph[20].append(32)
graph[32].append(32)
graph[5].append(21)
for i in range(21,24): graph[i].append(i+1)
graph[10].append(25)
graph[25].append(26)
graph[26].append(24)
graph[15].append(27)
graph[27].append(28)
graph[28].append(29)
graph[29].append(24)
graph[24].append(30)
graph[30].append(31)
graph[31].append(20)
score = [i*2 for i in range(21)]+[13,16,19,25,22,24,28,27,26,30,35,0]

result = 0
arr = tuple(map(int,input().split()))
solve([0,0,0,0],0,0)
print(result)