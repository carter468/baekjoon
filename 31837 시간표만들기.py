# 시간표 만들기
# Gold 4, bruteforcing, backtracking

def solve(idx,k):
    global count

    if k == 22: 
        count += 1
        return
    
    if idx == m or k > 22: 
        return

    for i in range(idx,m):
        g,c,d,s,e = arr[i]
        for group,day,start,end in tt:
            if g == group or (d == day and e > start and end > s):
                break
        else:
            tt.append((g,d,s,e))
            solve(i+1,k+c)
            tt.pop()

def minute(x):
    a,b = map(int,x.split(':'))
    return a*60+b

arr = []
for i in range(int(input())):
    for _ in range(int(input())):
        c,d,s,e = input().split()
        arr.append((i,int(c),d,minute(s),minute(e)))

m = len(arr)
count = 0
tt = []
solve(0,0)
print(count)