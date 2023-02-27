# IPv6
# Gold 5, 문자열

ipv6 = input().split(':')

l = len(ipv6)
c = 0
answer = []
for i in range(l):
    if ipv6[i]:
        answer.append(ipv6[i].zfill(4))
    elif c==0:
        c = 1
        for j in range(9-l):
            answer.append('0000')
    else:
        answer.append('0000')
        
print(':'.join(answer))