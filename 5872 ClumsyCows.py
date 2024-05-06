# Clumsy Cows
# Gold 5, greedy

a,b = 0,0
for c in input():
    if c == '(': b += 1
    elif b == 0:
        a += 1
        b += 1
    else:
        b -= 1
print(a+b//2)