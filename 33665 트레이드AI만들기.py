# 트레이드 AI 만들기
# Gold 5, implementation

W = [tuple(map(int,input().split())) for _ in range(10)]
before = list(input())
after = list(input())
mortgage = input()
cash = [int(input()) for _ in range(2)]
offer = [int(input()) for _ in range(2)]
A = int(input())
B = int(input())

result = 'YES'

for i in range(40):
    if after[i] == '0': after[i] = before[i]
    elif after[i] == '1' and before[i] != '2': result = 'NO'
    elif after[i] == '2' and before[i] != '1': result = 'NO'
if offer[0] > cash[0] or offer[1] > cash[1]: result = 'NO'

x = [0,0]
for i in range(10):
    a,b = 0,0
    for j in range(4):
        if before[i*4+j] == '1': a += 1
        elif before[i*4+j] == '2': b += 1
    if a: x[0] += W[i][a-1]
    if b: x[1] += W[i][b-1]

x[0] += cash[0]*A//100
x[1] += cash[1]*A//100

for i in range(40):
    if mortgage[i] == '1':
        if before[i] == '1': x[0] -= B
        else: x[1] -= B

y = [0,0]
for i in range(10):
    a,b = 0,0
    for j in range(4):
        if after[i*4+j] == '1': a += 1
        elif after[i*4+j] == '2': b += 1
    if a: y[0] += W[i][a-1]
    if b: y[1] += W[i][b-1]

cash[0] += offer[1]-offer[0]
cash[1] += offer[0]-offer[1]
y[0] += cash[0]*A//100
y[1] += cash[1]*A//100
for i in range(40):
    if mortgage[i] == '1':
        if after[i] == '1': y[0] -= B
        else: y[1] -= B

if y[0]-y[1] < x[0]-x[1]: result = 'NO'
print(result)