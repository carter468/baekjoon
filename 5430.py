# AC
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    a = input().strip()
    # 입력받은 a를 배열로 저장
    arr=[]
    temp = ''
    for x in a:     
        if x == '[':
            continue
        elif x == ',' or x==']':
            if temp != '':
                arr.append(int(temp))
                temp = ''
        else:
            temp += x    
    fward = True    #정방향인지 역방향인지 알수있는 변수
    err = False     #에러 발생여부

    for x in p:
        if x == 'R':    #뒤집기
            fward = not fward
        else:           # 버리기
            if len(arr) == 0:
                err = True
                break
            if fward:
                arr.pop(0)
            else:
                arr.pop()
    if err:
        print('error')
    elif fward:
        print(str(arr).replace(', ',','))
    else:
        print(str(list(reversed(arr))).replace(', ',','))
