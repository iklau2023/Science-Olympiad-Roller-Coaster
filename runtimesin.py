import math
d= float(input('What is the angle:'))
sin= math.sin(math.radians(d))
v= sin*18.2
t=364.5/v
t= round(t,2)
print(f'Your run time is {t} seconds')
