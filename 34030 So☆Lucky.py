# So☆Lucky
# Gold 3, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

answer = 'So Lucky'
odd,even = 0,0
for a in A:
    if a%2 == 0:
        if a < even:
            answer = 'Unlucky'
            break
        even = a
    else:
        if a < odd:
            answer = 'Unlucky'
            break
        odd = a
print(answer)

answer = 'So Lucky'
x,y = 0,A[0]
for i in range(1,N):
    if (A[i-1]+A[i])%2 == 1:
        x = y
    if A[i] < x:
        answer = 'Unlucky'
        break
    y = max(y,A[i])
print(answer)