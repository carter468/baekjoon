# 메이플스토리2 장례식
# Gold 3, geometry, bruteforcing, greedy, case work

for _ in range(int(input())):
    N = int(input())

    result = 6*N
    t = int(N**(1/3))
    for i in range(t,t//2,-1):
        for j in range(int(N**(1/2)),i-1,-1):
            for k in range(N//(i*j),j-1,-1):
                r = N-i*j*k
                if k < j or r > j*k: break
                if r == 0:
                    result = min(result,(i*j+j*k+k*i)*2)
                for x in range(int(r**0.5),0,-1):
                    y = r//x
                    if r-x*y > y: continue
                    z = r-x*y
                    if z > 0: a = (i*j+j*k+k*i)*2-r*2+(x*y+x+y)*2+(z*2+1)*2-z*2
                    else: a = (i*j+j*k+k*i)*2-r*2+(x*y+x+y)*2
                    result = min(result,a)
            else: continue
            break
    print(result)