# 바이러스 복제
# Gold 5, greedy

a,b = input(),input()

l = min(len(a),len(b))
c1,c2 = 0,0
for i in range(l):
    if a[i] == b[i]: c1 += 1
    else: break
for i in range(l):
    if a[-1-i] == b[-1-i]: c2 += 1
    else: break
if c1+c2 >= l: print(max(len(b)-len(a),0))
else: print(len(b)-c1-c2)
