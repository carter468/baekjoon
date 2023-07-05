# 전화번호 수수께끼(large)
# Gold 4, ad hoc

from collections import defaultdict
import sys
input = sys.stdin.readline

for t in range(int(input())):
    S = input()

    count = defaultdict(int)
    for x in S:
        count[x] += 1
    result = [0]*10
    result[0] = count['Z']
    result[2] = count['W']
    result[4] = count['U']
    result[6] = count['X']
    result[5] = count['F']-result[4]
    result[7] = count['V']-result[5]
    result[8] = count['G']
    result[3] = count['H']-result[8]
    result[1] = count['O']-result[4]-result[2]-result[0]
    result[9] = (count['N']-result[1]-result[7])//2

    answer = ''
    for i in range(10):
        answer += str(i)*result[i]

    print(f'Case #{t+1}: {answer}')