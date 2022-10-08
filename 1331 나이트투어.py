# 나이트투어

chess = []
chess.append(input())
check = ''
for _ in range(35):
    now = input()
    if now in chess:    # 갔던 곳 또 가기
        check = 'Invalid'
    if abs(ord(chess[-1][0]) - ord(now[0])) + abs(ord(chess[-1][1]) - ord(now[1])) != 3 or chess[-1][0] == now[0] or chess[-1][1] == now[1]:
        check = 'Invalid'    # 올바른 칸수를 갔나
    chess.append(now)
now = chess[0]
if not check:
    if abs(ord(chess[-1][0]) - ord(now[0])) + abs(ord(chess[-1][1]) - ord(now[1])) != 3 or chess[-1][0] == now[0] or chess[-1][1] == now[1]:
        check = 'Invalid'    # 마지막에서 처음으로 갈 수 있나
    else:
        check = 'Valid'
print(check)