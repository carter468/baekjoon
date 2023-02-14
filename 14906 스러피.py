# 스러피
# Gold 4, 재귀, 문자열, (정규표현식)

import sys
input = sys.stdin.readline

def slurpy():
    def slump(idx):
        try:
            if s[idx] not in ['D','E']:
                return 0
            if s[idx+1]!='F':
                return 0
            while s[idx+1]=='F':
                idx += 1
            if s[idx+1]=='G':
                return idx+1
            return slump(idx+1)    
        except:
            return 0
        
    def slimp(idx):
        try:
            if s[idx]!='A':
                return 0
            if s[idx+1]=='H':
                return idx+1
            if s[idx+1]=='B':
                a = slimp(idx+2)
                if a and s[a+1]=='C':
                    return a+1
                return 0
            else:
                a = slump(idx+1)
                if a and s[a+1]=='C':
                    return a+1
                return 0
        except:
            return 0    

    s = input().strip()
    a = slimp(0)
    if a==0:
        return 'NO'
    if slump(a+1)==len(s)-1:
        return 'YES'
    return 'NO'

print('SLURPYS OUTPUT')
for _ in range(int(input())):
    print(slurpy())
print('END OF OUTPUT')