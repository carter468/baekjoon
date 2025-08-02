# Rabbit Horse
# Gold 4, combinatorics, greedy, bruteforcing

N = int(input())
if N <= 11:
    print('rabbithorse'[:N])
else:
    result = [0]
    for i in range(N-10):
        arr = [(N-11-i)//9+1]*9
        for j in range((N-11-i)%9):
            arr[j] += 1
        x = (i+2)*(i+1)//2
        for a in arr:
            x *= a
        if x > result[0]: result = x,arr,i+2
    
    result[1].insert(2,result[2])
    for i,c in enumerate('rabithorse'):
        print(c*result[1][i],end='')