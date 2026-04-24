# 순열장난
# Gold 5, backtracking

def solve(arr,s):
    if not s:
        if set(arr) == set(range(1,max(arr)+1)):
            exit(print(*arr))
        else:
            return
    
    if s[0] == '0': return

    if int(s[0]) not in arr:
        arr.append(int(s[0]))
        solve(arr,s[1:])
        arr.pop()
    
    if len(s) >= 2 and int(s[:2]) not in arr:
        arr.append(int(s[:2]))
        solve(arr,s[2:])
        arr.pop()

solve([],input())