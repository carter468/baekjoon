# 0 만들기
# Gold 5, 브루트포스

def eval(exp):
    result = 0
    num = 0
    sign = 1
    for i in exp:
        if i == ' ': continue
        if i.isdigit():
            num = num*10+int(i)
        else:
            result += num*sign
            num = 0
            sign = (1 if i == '+' else -1)
    result += num*sign

    return result
        
def make_exp(exp,cnt):
    if cnt > n:
        if eval(exp) == 0:
            print(exp)
        return
    for i in (' ','+','-'):
        make_exp(exp+i+str(cnt),cnt+1)

t = int(input())
for i in range(t):
    n = int(input())
    make_exp('1',2)
    if i < t-1: print()