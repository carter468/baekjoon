# 구슬 놀이
# Platinum 4, ad hoc

N = 10**5
A = [N]
for i in range(1,448):
    A.extend([i]*i)
print(*A[:N])