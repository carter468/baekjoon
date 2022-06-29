#회의실 배정
import sys
input = sys.stdin.readline

# n = 11
# meeting = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int,input().split())))
meeting.sort()                      #시작 시간을 기준으로 정렬 후
meeting.sort(key=lambda x:x[1])     #끝나는 시간을 기준으로 정렬

end_time = -1           #끝나는시간은 0 이상
cnt = 0

for i in range(n):
    if end_time<=meeting[i][0]:     #끝나는 시간과 다음 시작 시간 비교
        end_time = meeting[i][1]
        cnt+=1

print(cnt)