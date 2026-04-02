# 종이접기
# Gold 3, implementation

input()
A = input().split()
a = [[int(input())]]

while A:
    x = A.pop()
    if x == 'R':
        a = [r[::-1]+r for r in a]
        for i in range(len(a)):
            for j in range(len(a[0])//2):
                if a[i][j] >= 2:
                    a[i][j] = 5-a[i][j]
                else:
                    a[i][j] = 1-a[i][j]
    elif x == 'L':
        a = [r+r[::-1] for r in a]
        for i in range(len(a)):
            for j in range(len(a[0])//2,len(a[0])):
                if a[i][j] >= 2:
                    a[i][j] = 5-a[i][j]
                else:
                    a[i][j] = 1-a[i][j]
    elif x == 'U':
        for c in a[::-1]:
            a.append(c[:])
        for i in range(len(a)//2,len(a)):
            for j in range(len(a[0])):
                if a[i][j] < 2:
                    a[i][j] += 2
                else:
                    a[i][j] -= 2
    elif x == 'D':
        a = [r[:] for r in a[::-1]]+a
        for i in range(len(a)//2):
            for j in range(len(a[0])):
                if a[i][j] < 2:
                    a[i][j] += 2
                else:
                    a[i][j] -= 2

for b in a:
    print(*b)