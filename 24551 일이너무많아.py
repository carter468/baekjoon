# 일이 너무 많아...
# Gold 3, 포함 배제의 원리, 수학

hate_number = [(10**i-1)//9 for i in [2,3,5,7,11,13,17]]

n = int(input())
answer = 0
for i,x in enumerate(hate_number):
    answer += n//x
    for j,y in enumerate(hate_number):
        if j<=i:
            continue
        if x*y>n:
            break
        answer -= n//(x*y)
        for k,z in enumerate(hate_number):
            if k<=j:
                continue
            if x*y*z>n:
                break
            answer += n//(x*y*z)
            for l,w in enumerate(hate_number):
                if l<=k:
                    continue
                if x*y*z*w>n:
                    break
                answer -= n//(x*y*z*w)

print(answer)