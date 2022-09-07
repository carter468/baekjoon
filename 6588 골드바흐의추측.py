m = 10**6
b = [False,False]+[True]*(m-1)
for i in range(2,m+1):
    if b[i]:
        for j in range(2*i,m+1,i):
            b[j] = False

while True:
    a = int(input())
    if a == 0:
        break
    
    for j in range(3,a//2+1,2):
        if b[j] and b[a-j]:
            print("{} = {} + {}".format(a,j,a-j))
            break