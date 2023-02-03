# 별꽃의 세레나데(Easy)
# Gold 5, 확률론, 기댓값의 선형성

result,e = 1,1
for i in range(int(input()),1,-1): 
    e *= i/(i-1)  
    result += e
print(result)