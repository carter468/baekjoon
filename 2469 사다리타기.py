# 사다리 타기
# Gold 5, implementation, backtracking

def solve(answer):
    if len(answer) == k-1:
        for i in range(k):
            a = r1[i]
            if a == 0:
                if answer[a] == '-':
                    a += 1
            elif a == k-1:
                if answer[a-1] == '-':
                    a -= 1
            elif answer[a] == '-':
                a += 1
            elif answer[a-1] == '-':
                a -= 1
            
            if i != s[r2[a]]: return
        print(answer)
        exit()
    
    if not answer or answer[-1] == '*':
        solve(answer+'-')
    solve(answer+'*')

k,n = int(input()),int(input())
s = list(input())
arr = [input() for _ in range(n)]

for i in range(k):
    s[i] = ord(s[i])-65

r1,r2 = [-1]*k,[-1]*k
for i in range(k):
    ni = i
    for j in range(n):
        if arr[j][0] == '?': break
        if ni == 0:
            if arr[j][ni] == '-':
                ni += 1
        elif ni == k-1:
            if arr[j][ni-1] == '-':
                ni -= 1
        elif arr[j][ni] == '-': ni += 1
        elif arr[j][ni-1] == '-': ni -= 1
    r1[i] = ni

    ni = i
    for j2 in range(j+1,n):
        if arr[j2][0] == '?': break
        if ni == 0:
            if arr[j2][ni] == '-':
                ni += 1
        elif ni == k-1:
            if arr[j2][ni-1] == '-':
                ni -= 1
        elif arr[j2][ni] == '-': ni += 1
        elif arr[j2][ni-1] == '-': ni -= 1
    r2[i] = ni

solve('')
print('x'*(k-1))