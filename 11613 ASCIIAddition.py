# ASCII Addition
# Gold 5, implementation

NUM = [['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx'],
       ['....x','....x','....x','....x','....x','....x','....x'],
       ['xxxxx','....x','....x','xxxxx','x....','x....','xxxxx'],
       ['xxxxx','....x','....x','xxxxx','....x','....x','xxxxx'],
       ['x...x','x...x','x...x','xxxxx','....x','....x','....x'],
       ['xxxxx','x....','x....','xxxxx','....x','....x','xxxxx'],
       ['xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx'],
       ['xxxxx','....x','....x','....x','....x','....x','....x'],
       ['xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx'],
       ['xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx']]

def find(idx):
    for i in range(10):
        for j in range(7):
            if arr[j][idx*6:idx*6+5] != NUM[i][j]:
                break
        else:
            return str(i)
    return ' '

arr = [input() for _ in range(7)]
result = ''
for i in range((len(arr[0])+1)//6):
    result += find(i)

a,b = map(int,result.split())
result = str(a+b)
l = len(result)
for i in range(7):
    for j in range(l):
        if j != l-1:
            print(NUM[int(result[j])][i]+'.',end='')
        else:
            print(NUM[int(result[j])][i])