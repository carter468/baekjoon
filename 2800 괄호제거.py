# 괄호 제거
# Gold 4, bruteforcing, bitmasking

s = input()

l = len(s)
arr = []
stack = []
for i in range(l):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        arr.append((stack.pop(),i))

c = s.count('(')
result = set()
for i in range(1,1<<c):
    string = ''
    temp = set()
    for k in range(c):
        if i>>k&1:
            temp.add(arr[k][0])
            temp.add(arr[k][1])
            
    for j in range(l):
        if j not in temp:
            string += s[j]
    result.add(string)

print('\n'.join(sorted(result)))