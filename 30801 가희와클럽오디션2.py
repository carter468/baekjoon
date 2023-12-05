# 가희와 클럽 오디션 2
# Gold 5, implementation, parsing

dic = {'W':'W8','W!':'S2','S':'S2','S!':'W8','A':'A4','A!':'D6','D':'D6','D!':'A4',
       'LU':'7','LU!':'3','LD':'1','LD!':'9','RU':'9','RU!':'1','RD':'3','RD!':'7'}

a,b = input(),input()

i = 0
aa = []
while i < len(a):
    temp = ''
    while temp not in dic:
        temp += a[i]
        i += 1
    if i < len(a) and a[i] == '!':
        temp += '!'
        i += 1
    aa.append(temp)

i,j = 0,0
count = 0
while j < len(b):
    if i == len(aa) or b[j] not in dic[aa[i]]:
        count = 0
        i = 0
    elif b[j] in dic[aa[i]]:
        count += 1
        i += 1
    j += 1

if count == len(aa): print('Yes')
else: print('No')