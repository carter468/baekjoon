# 측량사 지윤
# Gold 3, geometry

def intersection(i,j):
    a1,b1,c1 = arr[i]
    a2,b2,c2 = arr[j]
    if a1*b2 == a2*b1: return False
    return (b1*c2-b2*c1)/(a1*b2-a2*b1),(a1*c2-a2*c1)/(a2*b1-a1*b2)

for _ in range(int(input())):
    arr = [tuple(map(int,input().split())) for _ in range(3)]
    a,b,c = intersection(0,1),intersection(1,2),intersection(2,0)
    if False in (a,b,c): print('0.0000')
    else: print(f'{abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-b[0]*a[1]-c[0]*b[1]-a[0]*c[1])/2:.4f}')