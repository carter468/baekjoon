# 초콜릿 보물 찾기
# Gold 2, ad hoc

import sys
input = sys.stdin.readline

def query(q):
    for x,y in q:
        print('?',x,y)
        sys.stdout.flush()
        if int(input()):
            print('!',x,y,i,j)
            exit()

for i in range(10):
    for j in range(i%2,10,2):
        if i+j in (0,18): continue
        print('?',i,j)
        sys.stdout.flush()
        if int(input()):
            if i == 0: 
                query([(i,j-1),(i,j+1)])
                print('!',i,j,i+1,j)
            elif i == 9:
                query([(i,j-1),(i,j+1)])
                print('!',i,j,i-1,j)
            elif j == 0:
                query([(i-1,j),(i+1,j)])
                print('!',i,j,i,j+1)
            elif j == 9:
                query([(i-1,j),(i+1,j)])
                print('!',i,j,i,j-1)
            else:
                query([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
            exit()

print('? 0 0')
sys.stdout.flush()
if int(input()):
    print('? 0 1')
    sys.stdout.flush()
    if int(input()):
        print('! 0 0 0 1')
    else:
        print('! 0 0 1 0')
else:
    print('? 9 8')
    sys.stdout.flush()
    if int(input()):
        print('! 9 8 9 9')
    else:
        print('! 8 9 9 9')