x = int(input('eneter the number whose factor you want to check: '))
y = int(input('enter the factor you want to check: '))
if(x%y == 0):
    print(y , 'is a factor of ' , x)
else:
    print(y , 'is not a factor of ' , x)
