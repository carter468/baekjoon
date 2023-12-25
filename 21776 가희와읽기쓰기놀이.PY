# 가희와 읽기 쓰기 놀이
# Gold 3, backtracking, implementation

n,c = map(int,input().split())
card = [tuple(map(int,input().split())) for _ in range(n)]
oper = [0]+[input().split(',') for _ in range(c)]

def operation(s,p):
    for q in p:
        if q[0] == 'A':
            s = s+q[4:]
        else:
            if (int(q[4])) >= len(s):
                return 'ERROR'
            else:
                temp = ''
                for j in range(len(s)):
                    if j != int(q[4]):
                        temp += s[j]
                s = temp
    return s

def play(s):
    if sum(visited) == c:
        if 1 not in idx:
            if s == '': s = 'EMPTY'
            result.add(s)
        return

    for i in range(n):
        if idx[i] <= card[i][0] and visited[card[i][idx[i]]] == 0:
            temp = operation(s,oper[card[i][idx[i]]])
            if temp == 'ERROR':
                result.add(temp)
                continue
            visited[card[i][idx[i]]] = 1
            idx[i] += 1
            play(temp)
            idx[i] -= 1
            visited[card[i][idx[i]]] = 0

idx = [1]*n 
result = set()
visited = [0]*(c+1) 
play('')
print('\n'.join(sorted(result)))