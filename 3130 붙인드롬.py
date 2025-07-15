# 붙인드롬
# Gold 4, bruteforcing, number theory

N,M = map(int,input().split())

count = [0]*M
n = N//2
for i in range(10**((n+1)//2)):
    i = str(i).zfill((n+1)//2)
    count[int(i+i[-1-(n%2)::-1])%M] += 1

result = 0
for i in range(10**((n+1)//2-1),10**((n+1)//2)):
    i = str(i).zfill((n+1)//2)
    result += count[-(int(i+i[-1-(n%2)::-1])*10**n%M)]
print(result)