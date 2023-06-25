# A와 B
# Gold 5, greedy

s,t = list(input()),list(input())

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]
        
print(1 if s==t else 0)