# Router

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
buffer_packet = deque()
while True:
    input_packet = input().strip()
    if input_packet == '-1':
        break
    elif input_packet == '0':
        buffer_packet.popleft()
    elif len(buffer_packet) != n:
        buffer_packet.append(input_packet)
if buffer_packet:
    print(*buffer_packet)
else:
    print('empty')