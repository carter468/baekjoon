# 테니스
# Gold 2, implementation, case work

def solve():
    arr = input().split()

    score = [0,0]

    for i in range(len(arr)):
        a,b = map(int,arr[i].split(':'))
        if i == 2 and 2 in score or a == b or i > 2:
            return 'ne'

        c,d = max(a,b),min(a,b)
        if i < 2: 
            if c < 6 or c > 7: 
                return 'ne'
            if c == 6 and d > 4: 
                return 'ne'
            if c == 7 and d not in (5,6): 
                return 'ne'
        else: 
            if c < 6: 
                return 'ne'
            if c == 6 and d > 4: 
                return 'ne'
            if c > 6 and c-d != 2: 
                return 'ne'
            
        if a > b:
            if name[1] == 'federer': return 'ne'
            score[0] += 1
        else:
            if name[0] == 'federer': return 'ne'
            score[1] += 1

    if 2 in score: return 'da'
    else: return 'ne'

name = input().split()

for _ in range(int(input())):
    print(solve())