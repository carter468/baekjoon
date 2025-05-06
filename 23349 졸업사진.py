# 졸업 사진
# Gold 5, prefix sum, implementation

M = 50000

name = set()
place = dict()
for _ in range(int(input())):
    n,p,s,e = input().split()
    if n in name: continue
    name.add(n)
    s,e = int(s),int(e)
    if p not in place: place[p] = [0]*(M+2)
    place[p][s] += 1
    place[p][e] -= 1

result = []
m = 0
for p in place:
    for i in range(M):
        place[p][i+1] += place[p][i]
    s = 0
    for i in range(M+1):
        if place[p][i] != place[p][s]: 
            if place[p][s] > m:
                result = [(p,s,i)]
                m = place[p][s]
            elif place[p][s] == m:
                result.append((p,s,i))
            s = i
    if place[p][s] > m:
        result = [(p,s,M)]
        m = place[p][s]
    elif place[p][s] == m:
        result.append((p,s,M))

print(*sorted(result)[0])