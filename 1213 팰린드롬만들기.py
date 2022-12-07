# 팰린드롬만들기
# Silver 3, 그리디알고리즘, 문자열

def solve():
    s = input()
    c = sorted(set(s))
    answer = ''
    f = ''
    for x in c:
        count = s.count(x)
        if count%2:
            if f:
                print('I\'m Sorry Hansoo')
                return
            f = x
        answer += x*(count//2)
    print(answer+f+answer[::-1])
solve()