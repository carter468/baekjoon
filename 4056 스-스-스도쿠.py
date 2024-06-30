# 스-스-스도쿠
# Gold 4, backtracking, implementation

def check(arr):
    for a in range(3):
        for b in range(3):
            temp = set()
            for c in range(3):
                for d in range(3):
                    temp.add(arr[a*3+c][b*3+d])
            if len(temp) != 9:
                return False
    
    for a in range(9):
        temp1,temp2 = set(),set()
        for b in range(9):
            temp1.add(arr[a][b])
            temp2.add(arr[b][a])
        if len(temp1) != 9 or len(temp2) != 9: return False
        
    return True

def solve(idx,arr):
    if idx == 5:
        if check(arr):
            return arr
        return
    
    x,y = e[idx]
    for i in range(1,10):
        arr[x][y] = str(i)
        result = solve(idx+1,arr)
        if result: return result
        arr[x][y] = '0'

for _ in range(int(input())):
    arr = [list(input()) for _ in range(9)]

    e = []
    for i in range(9):
        for j in range(9):
            if arr[i][j] == '0':
                e.append((i,j))
    
    result = solve(0,arr)
    if result:
        for r in result:
            print(''.join(r))
    else: 
        print('Could not complete this grid.')
    print()