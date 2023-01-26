h= float(input('What is the height of the roller coaster in cm:'))
hs= 2*(60-h)
g= float(input('How long is your gap in cm:'))
if g < 5 :
    l=float(input('How tall is your loop in cm:'))
    gs=0
elif g >= 5:
    gs= g*4
    l=float(input('How tall is your loop in cm:'))
ls= l*6
rt = float(input('What is the given run time in seconds:'))
t= int(input('What is your time:'))
ts= t*5
if t>rt:
    ts= ts*-5
s= hs+gs+ls+ts
print(f'Your final score is {s}')
