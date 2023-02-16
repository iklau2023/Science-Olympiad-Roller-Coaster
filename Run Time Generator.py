import random
user = input('State , Regionals or Nationals:').lower()
if user == 'state':
    time= [30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]
    x= random.choice(time)
    print(f'Your time is {x}')    
if user == 'regionals':
    time= [30,35,40,45,50,55,60]
    x= random.choice(time)
    print(f'Your time is {x}')
if user == 'nationals':
    x= random.randrange(30,60)
    print(f'Your time is {x}') 
