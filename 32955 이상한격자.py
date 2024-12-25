# 이상한 격자
# Gold 3, bruteforcing, prefix sum

N,A,B,C,D = map(int,input().split())
X,Y = [],[]
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
psum_x,psum_y = [0],[0]
for i in range(N):
    psum_x.append(psum_x[i]+X[i])
    psum_y.append(psum_y[i]+Y[i])
rx,ry = 10**20,10**20
for i in range(N):
    x = (i*X[i]-psum_x[i])*B+(psum_x[-1]-psum_x[i+1]-(N-1-i)*X[i])*A
    y = (i*Y[i]-psum_y[i])*D+(psum_y[-1]-psum_y[i+1]-(N-1-i)*Y[i])*C
    rx = min(rx,x)
    ry = min(ry,y)
print(rx+ry)