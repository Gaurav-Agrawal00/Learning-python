a = int(input('enter your year '))
if(a % 4 == 0 and a %100 != 0):
    print('leap year')
elif( a% 4 == 0 and a% 10 == 0 and a%400 == 0 ):
    print('A leap Year')
else:
    print('not a leap year')