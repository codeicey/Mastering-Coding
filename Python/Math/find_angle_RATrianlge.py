import math
AB,BC=int(input()),int(input())

hype=math.hypot(AB,BC)                    #hypotenuse of AB, BC
res=round(math.degrees(math.acos(BC/hype)))  #acos for radian, degrees for converting radian to degrees

degree=chr(176)                           #degree in ASCII   
print(res,degree, sep='')

