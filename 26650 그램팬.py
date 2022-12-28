# 그램팬
# Silver 1, 문자열

idx = 65
na,nz = 0,0
result = 0
for char in input():
    if ord(char) == idx or ord(char) == idx+1:
        idx = ord(char)
        if char == 'Z':
            nz += 1
    else:
        result += na*nz
        idx = 65
        na,nz = 0,0
    if char == 'A':
        na += 1

print(result+na*nz)