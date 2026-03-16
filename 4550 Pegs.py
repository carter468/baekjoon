# Pegs
# Gold 3, bruteforcing, DFS

for _ in range(int(input())):
    grid = [input() for _ in range(5)]

    pound = set()
    peg = []
    for i in range(5):
        for j in range(5):
            if grid[i][j] == '#':
                pound.add(i*5+j)
            elif grid[i][j] == 'o':
                peg.append(i*5+j)

    peg = tuple(sorted(peg))
    visited = {peg}
    q = [peg]
    result = 25
    while q:
        x = q.pop()
        result = min(result,len(x))
        for a in x:
            for k in (5,-5,1,-1):
                b = a+k
                c = b+k
                if abs(k) == 1 and a//5 != c//5: continue
                if b in x and 0 <= c < 25 and c not in x and c not in pound:
                    nx = set(x)
                    nx.remove(a)
                    nx.remove(b)
                    nx.add(c)
                    nx = tuple(sorted(nx))
                    if nx not in visited:
                        q.append(nx)
                        visited.add(nx)
    print(f'The best case ends with {result} pegs.')