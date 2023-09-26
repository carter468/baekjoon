# 문자열 만들기 1
# Gold 4, ad hoc, constructive, stack

input()
t = list(input())

count = 0
result = []
temp = []
while t:
    c = t.pop()
    if not temp or c != temp[-1]:
        if c == 'U':
            result.append('SN')
            count += 2
            temp.append('S')
        else:
            result.append('UN')
            count += 2
            temp.append('U')
    else:
        result.append('N')
        count += 1
        temp.pop()

print(count)
print(''.join(result))