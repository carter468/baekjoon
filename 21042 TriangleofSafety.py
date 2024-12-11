# Triangle of Safety
# Platinum 5, ad hoc

N = 25
for i in range(N):
    for a,b in (1,3),(4,11),(5,13),(6,15):
        print(chr(i+65)+chr((i+a)%N+65)+chr((i+b)%N+65))