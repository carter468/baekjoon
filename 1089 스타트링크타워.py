# 스타트링크 타워
# Gold 4, 확률론

def compare(idx,num):
    for i in range(5):
        for j in range(3):
            if numbers[i][4*num+j] == '.' and board[i][4*idx+j] == '#':
                return False
    return True

numbers = ['###...#.###.###.#.#.###.###.###.###.###',
           '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
           '#.#...#.###.###.###.###.###...#.###.###',
           '#.#...#.#.....#...#...#.#.#...#.#.#...#',
           '###...#.###.###...#.###.###...#.###.###']

n = int(input())
arr = [[] for _ in range(n)]
board = [input() for _ in range(5)]
for i in range(n):
    for j in range(10):
        if compare(i,j):
            arr[i].append(j)

result = 0
for i in arr:
    if not i:
        result = -1
        break
    result = result*10 + sum(i)/len(i)
print(result)