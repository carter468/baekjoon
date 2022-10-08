# 자전거 속도

value_pi = 3.1415927
mile_inch = 5280*12
i = 1
while True:
    d,r,t = map(float,input().split())
    if r==0:
        break
    d *= value_pi*r/mile_inch
    t /= 3600
    v = d/t
    print("Trip #{}: {:.2f} {:.2f}".format(i,d,v))
    i += 1