# 전화번호 수수께끼 (Small)
# Gold 5, bruteforcing

def solve(n,s,idx): 
    if len(s) > 20: return 
    answer[tuple(sorted(list(s)))] = n
    for i in range(idx,10):
        solve(n+str(i),s+num[i],i)

answer = {}
num = {0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
solve('','',0)

for i in range(int(input())): 
    print(f'Case #{i+1}: {answer[tuple(sorted(list(input())))]}')