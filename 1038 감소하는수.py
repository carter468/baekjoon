# 감소하는 수

n = int(input())

def dec(i,num):
    global cnt
    if len(num) == i:
        cnt += 1
        if cnt == n:
            print(num)
            quit()
        return
    for k in range(int(num[-1])):
        dec(i,num+str(k))
    
if n<10:
    print(n)
else:
    i = 2
    cnt = 9
    while True:
        if i>10:
            print(-1)
            break
        for j in range(1,10):
            dec(i,str(j))
        i += 1