# Numbers (Small)
# Gold 3, math

result = [0,0]
a,b = 3,1
for _ in range(29):
    a,b = a*3+b*5,a+b*3
    result.append(str((2*a-1)%1000).zfill(3))    

for i in range(int(input())):
    print(f'Case #{i+1}: {result[int(input())]}')