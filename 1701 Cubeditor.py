# Cubeditor
# Gold 3, KMP

def findLen(s):
    global result
    p = [0]*len(s)
    j = 0
    for i in range(1,len(s)):
        while j > 0 and s[i] != s[j]:
            j = p[j-1]
        if s[i] == s[j]:
            j += 1
            p[i] = j
    result = max(result,max(p))

S = input()

result,i = 0,0
while i < len(S)-result*2:
    findLen(S[i:])
    i += 1

print(result)