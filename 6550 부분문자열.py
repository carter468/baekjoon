# 부분 문자열
# Silver 5

while True:
    try:
        s,t = input().split()
        idx = 0
        for ss in s:
            for i in range(idx,len(t)):
                if ss==t[i]:
                    idx = i+1
                    break
            else:
                print('No')
                break
        else:
            print('Yes')
    except:
        break