# Treasure
# Gold 5, Stack

n,k = map(int,input().split())
s = input()

result = []
count = [['']]
for c in s:
    result.append(c)
    
    if c == count[-1][0]:
        count[-1][1] += 1
    else:
        count.append([c,1])

    if count[-1][1] == k:
        for i in range(k):
            result.pop()
        count.pop()

print(''.join(result))