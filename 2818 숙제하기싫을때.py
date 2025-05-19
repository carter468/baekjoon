# 숙제하기 싫을 때
# Gold 4, simulation, implementation

R,C = map(int,input().split())

dice = [1,4,6,3,5,2]
x,y = divmod(C-1,4)
result = 0
for i in range(R):
    if i%2 == 0:
        result += sum(dice[:4])*x+sum(dice[:y+1])
        dice = dice[y:4]+dice[:y]+dice[4:]
    else:
        result += sum(dice[:4])*x+dice[0]
        if y:
            result += sum(dice[-2-y:-2])
            dice = dice[-2-y:4]+dice[:-2-y]+dice[4:]
    dice = [dice[4],dice[1],dice[5],dice[3],dice[2],dice[0]]
print(result)