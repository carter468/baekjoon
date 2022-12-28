# 그램팬
# Silver 1, 문자열

import sys

idx = 65
na = 0
result = 0
for char in sys.stdin.readline():
    if ord(char) == idx or ord(char) == idx+1:
        idx = ord(char)
        if char == 'Z':
            result += na
    else:
        idx = 65
        na = 0
    if char == 'A':
        na += 1

print(result)