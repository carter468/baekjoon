# Гирлянда
# Platinum 4, binary search

N = int(input())+1
S = '1'+input()

idx = []
psum = [0]
for i in range(N):
    psum.append(psum[-1])
    if S[i] == '0':
        psum[-1] += 1
    else:
        idx.append(i)

result = 0,
for i in range(N//2): # 연속0의개수
    j = 0 # 몇번째1까지 보았는가
    c = 0 # 선택된 1의 개수
    while j < len(idx) and idx[j]+i < N:
        no,yes = j,len(idx)
        while no+1 < yes:
            mid = (no+yes)//2
            if psum[idx[mid]]-psum[idx[j]] >= i: yes = mid
            else: no = mid
        j = yes
        if j == len(idx) or psum[-1]-psum[idx[j]] < i: break
        c += 1
    
    l = i*c+i+c
    if c > 0 and l > result[0]: 
        result = l,('0'*i+'1')*c+'0'*i

print(*result,sep='\n')