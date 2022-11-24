# 2877 4와 7
# Gold 5

k = int(input())
answer = ''
answer_length = 1

# 답이 몇자리인지 구하기
while 2**(answer_length+1)-2<k:
    answer_length += 1

# answer_length 길이의 숫자 중 x번째 수가 answer
x = k-2**(answer_length)+1

# 뒷자리부터 4,7 결정
for _ in range(answer_length):
    answer = '47'[x%2] + answer
    x //= 2
print(answer)