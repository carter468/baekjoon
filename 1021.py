#회전하는 큐

def rotate_r():     # 오른쪽 회전 : 마지막원소가 처음으로 이동
    que.insert(0,que[-1])
    que.pop()
    return
def rotate_l():     # 왼쪽 회전 : 처음원소가 마지막으로 이동
    que.append(que[0])
    que.pop(0)
    return

n,m = map(int,input().split())
num_pop = list(map(int,input().split()))

que = [x+1 for x in range(n)]
len_q = n
ans = 0

for x in num_pop:
    if que[0] == x:     # 바로 뽑는 경우
        que.pop(0)
        len_q -= 1
    else:               # 회전해야하는경우
        for i in range(1,len_q):    #뽑을 수의 위치찾기
            if que[i] == x:
                break
        if i < len_q / 2:      # 왼쪽에 가까우면 왼쪽회전
            for _ in range(i): 
                rotate_l()
                ans += 1
        else:
            for _ in range(len_q-i):  #오른쪽에 가까우면 오른쪽회전
                rotate_r()
                ans += 1
        que.pop(0)
        len_q -= 1

print(ans)