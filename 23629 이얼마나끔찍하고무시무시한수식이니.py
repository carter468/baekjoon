# 이 얼마나 끔찍하고 무시무시한 수식이니
# Gold 5, implementation

dic = {'ONE':'1','TWO':'2','THREE':'3','FOUR':'4','FIVE':'5','SIX':'6','SEVEN':'7','EIGHT':'8','NINE':'9','ZERO':'0',
       '1':'ONE','2':'TWO','3':'THREE','4':'FOUR','5':'FIVE','6':'SIX','7':'SEVEN','8':'EIGHT','9':'NINE','0':'ZERO','-':'-'}

S = input()

answer = ''
result = 0
temp = ''
now = ''
op = ''
for c in S:
    if c in '+-/x=':
        answer += c
        if now == '' or temp:
            print('Madness!')
            break
        if op == '':
            result = int(now)
        if op == '+':
            result += int(now)
        elif op == '-':
            result -= int(now)
        elif op == 'x':
            result *= int(now)
        elif op == '/':
            result = int(result/int(now))
        op = c
        now = ''
    else:
        temp += c
        if temp in dic:
            now += dic[temp]
            answer += dic[temp]
            temp = ''
else:
    print(answer)
    for c in str(result):
        print(dic[c],end='')