# 오늘은 OS 숙제 제출일

def ly(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    return False
def output(x,m,d,y):
    if y<1999 or y>2201:
        print('OUT OF RANGE')
    elif x == 0:
        print('SAME DAY')
    elif x == 1:
        print(f"{m}/{d}/{y} IS {x} DAY PRIOR")
    elif x == -1:
        print(f"{m}/{d}/{y} IS {-x} DAY AFTER")
    elif 1 < x < 8:
        print(f"{m}/{d}/{y} IS {x} DAYS PRIOR")
    elif -8 < x < -1:
        print(f"{m}/{d}/{y} IS {-x} DAYS AFTER")
    else:
        print('OUT OF RANGE')
month = [31,31,28,31,30,31,30,31,31,30,31,30,31]
t = int(input())
for _ in range(t):
    due,admit = map(str,input().split())
    due_month,due_date,due_year = map(int,due.split('/'))
    admit_month,admit_date = map(int,admit.split('/')) 
    if due_month == 1 and admit_month == 12:    # 1월 마감 12월 제출
        dif = due_date-admit_date+31
        output(dif,admit_month,admit_date,due_year-1)   
    elif due_month == 12 and admit_month == 1:  # 12월 마감 1월 제출
        dif = due_date-admit_date-31
        output(dif,admit_month,admit_date,due_year+1)
    elif abs(due_month-admit_month) >= 2:
        print('OUT OF RANGE')
    else:
        dif = due_date-admit_date
        if due_month>admit_month:
            dif += month[admit_month]
            if ly(due_year) and admit_month == 2:
                dif += 1
        elif due_month<admit_month:
            dif -= month[due_month]
            if ly(due_year) and due_month == 2:
                dif -= 1
        output(dif,admit_month,admit_date,due_year)