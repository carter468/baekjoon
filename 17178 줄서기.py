from collections import deque
import sys
input = sys.stdin.readline

waiting = deque()
for _ in range(int(input())):
    for ticket in input().split():
        a,b = ticket.split('-')
        waiting.append((a,int(b)))
ticket_order = deque(sorted(waiting))

stack = deque()
answer = 'GOOD'
while ticket_order:
    now = ticket_order.popleft()
    while True:
        if stack and stack[-1]==now:
            stack.remove(now)
            break
        if waiting:
            stack.append(waiting.popleft())
        else:
            answer = 'BAD'
            break
    if answer == 'BAD':
        break
print(answer)