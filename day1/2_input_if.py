age = int(input('How old are you?   '))
print(f'you are {age} years old')

if age < 18:
    print(f'You will be grown up in {18 - age} years')
elif age == 18:
    print(f'You are just grown up')
else:
    print(f'You are adult')
    
print('done')
    
    
