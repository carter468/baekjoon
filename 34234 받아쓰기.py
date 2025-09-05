# 받아쓰기
# Platinum 5, constructive, case work, greedy

def finish():
    while arr1:
        i = arr1.pop()
        result[i] = Ss[i]
    while arr2:
        i = arr2.pop()
        for a in 'abc':
            if a != Ss[i] and a != Sk[i]:
                result[i] = a
    print(''.join(result))

N = int(input())
Ss,Sk,Sh = input(),input(),input()

result = [0]*N
score = [0]*2
arr1 = []
arr2 = []
for i in range(N):
    s,k,h = Ss[i],Sk[i],Sh[i]
    if s == k == h:
        result[i] = s
    elif k == h:
        result[i] = s
        score[0] += 1
    elif s == k:
        result[i] = s
        score[0] += 1
        score[1] += 1
    elif s == h:
        arr2.append(i)
    else: arr1.append(i)

if score[1] == 0:
    if arr2:
        i = arr2.pop()
        result[i] = Sk[i]
    elif arr1:
        i = arr1.pop()
        result[i] = Sk[i]
    else:
        exit(print(-1))
    score[1] = 1

if score[0] > score[1]:
    finish()
elif score[0] == score[1]:
    if arr1:
        finish()
    else:
        if score[1] == 1 or not arr2:
            print(-1)
        else:
            i = arr2.pop()
            result[i] = Ss[i]
            finish()
else:
    if len(arr1) < 2: print(-1)
    else: finish()