a = int(input('Enter first side'))
b = int(input('Enter second side'))
c = int(input('Enter third side'))

if(a+b > c and b+c > a and c+a > b):
    print('it is a triangle')
else:
    print("it's side does not follow triangle property")