# 문자열 변환
# Gold 5, ad hoc

for _ in range(int(input())):
    A,B = input().split()
    if len(A) != len(B): print(-1)
    else:
        result = 0
        a,b = [],[]
        for i in range(len(A)):
            if A[i] == 'a': a.append(i)
            if B[i] == 'a': b.append(i)
        for i in range(len(A)//2):
            result += abs(a[i]-b[i])
        print(result)