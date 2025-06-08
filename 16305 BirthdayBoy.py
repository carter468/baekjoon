# Birthday Boy
# Gold 5, impelmentation, ad hoc

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

N = int(input())
arr = []
for _ in range(N):
    mm,dd = map(int,input().split()[1].split('-'))
    arr.append(sum(month[:mm])+dd)
arr.sort()
arr.append(arr[0]+365)

m = 2
d = []
for i in range(N):
    if arr[i+1]-arr[i] > m:
        m = arr[i+1]-arr[i]
        d = [(arr[i+1]-302)%365]
    elif arr[i+1]-arr[i] == m:
        d.append((arr[i+1]-302)%365)
d = sorted(d)[0]+301
if d > 365: d -= 365
for i in range(13):
    if month[i] < d: d -= month[i]
    else: break
print(f'{i:02}-{d:02}')