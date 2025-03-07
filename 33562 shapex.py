# shapex
# Platinum 5, implementation

import sys
input = sys.stdin.readline

def merge(x,y):
    result = ''
    for i in range(8):
        if x[i] != '-' and y[i] != '-': return ''
        if x[i] != '-': result += x[i]
        else: result += y[i]
    return result

N,M = map(int,input().split())
arr = ['None']*101
for i in range(1,N+1):
    arr[i] = input().strip()

for _ in range(M):
    a,i,j,k = input().split()
    if a == '1':
        i,j,k = int(i),int(j),int(k)
        l,r = [],[]
        if arr[i] != 'None':
            for shape in arr[i].split(':'):
                s1,s2 = shape[4:],shape[:4]
                if s1 != '----': l.append('----'+s1)
                if s2 != '----': r.append(s2+'----')
        arr[j] = ':'.join(l) if l else 'None'
        arr[k] = ':'.join(r) if r else 'None'
    elif a == '2':
        i,j,k = int(i),int(j),int(k)
        if arr[i] != 'None':
            new = []
            for shape in arr[i].split(':'):
                new.append(shape[-k*2:]+shape[:-k*2])
            arr[j] = ':'.join(new)
        else:
            arr[j] = 'None'
    elif a == '3':
        i,j,k = int(i),int(j),int(k)
        if arr[i] != 'None' and arr[j] != 'None':
            shape_i = arr[i].split(':')
            shape_j = arr[j].split(':')
            new = shape_i+shape_j
            flag = False
            for l in range(len(shape_i)-1,-1,-1):
                temp = shape_i[:l]
                for idx in range(len(shape_j)):
                    if idx+l >= len(shape_i):
                        temp += shape_j[idx:]
                        break
                    r = merge(shape_i[idx+l],shape_j[idx])
                    if not r:
                        flag = True
                        break
                    temp.append(r)
                if flag: break
                if l+len(shape_j) < len(shape_i):
                    temp += shape_i[l+len(shape_j)-len(shape_i):]
                new = temp
            if len(new) > 4: new = new[:4]
            arr[k] = ':'.join(new)
        else:
            arr[k] = 'None'
    elif a == '4':
        i,j = int(i),int(j)
        if arr[i] != 'None':
            new = []
            for shape in arr[i].split(':'):
                s = ''
                for i in range(8):
                    if i%2 == 0:
                        s += shape[i]
                    elif shape[i] != '-':
                        s += k
                    else:
                        s += '-'
                new.append(s)
            arr[j] = ':'.join(new)
        else:
            arr[j] = 'None'
        
print(arr[100])