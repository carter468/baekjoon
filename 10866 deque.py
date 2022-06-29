# 덱
import sys

n = int(sys.stdin.readline())
deq = [0]*20000
front = 10001
back = 10000

for _ in range(n):
    order = list(map(str,sys.stdin.readline().rstrip().split()))
    if order[0] == 'push_front': #push_front x
        front -= 1
        deq[front] = order[1]
        
    elif order[0] == 'push_back': #push_back x
        back += 1
        deq[back] = order[1]
    elif order[0] == 'pop_front': #pop_front
        if front>back:
            print(-1)
        else:
            print(deq[front])
            front += 1
    elif order[0] == 'pop_back': #pop_back
        if front>back:
            print(-1)
        else:
            print(deq[back])
            back -= 1
    elif order[0] == 'size': #size
        print(back-front+1)
    elif order[0] == 'empty': #size
        print(int(front>back))
    elif order[0] == 'front': #front
        if front>back:
            print(-1)
        else:
            print(deq[front])
    elif order[0] == 'back': #back
        if front>back:
            print(-1)
        else:
            print(deq[back])