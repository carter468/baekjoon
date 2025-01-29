# 편안한 수열 만들기
# Gold 3, case work, ad hoc, constructive

N,K = map(int,input().split())

if N == 2:
    print('YES',*['swap 1 2']*5,sep='\n')
elif N == 3:
    print('NO')
elif K > 1 and N-K > 1:
    print('YES',f'reverse 1 {K}',f'reverse {K+1} {N}',*[f'reverse 1 {N}']*3,sep='\n')
elif K == 1:
    print('YES','swap 1 2',f'reverse 2 {N}',*[f'reverse 2 {N-1}']*3,sep='\n')
elif N-K == 1:
    print('YES',f'swap {N-1} {N}',f'reverse 1 {N-1}',*[f'reverse 2 {N-1}']*3,sep='\n')