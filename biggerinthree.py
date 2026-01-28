a= int(input('enter your first number'))
b= int(input('enter your second number'))
c= int(input('enter your third number '))
if(a>b and a>c):
    print(a,' is greater then ', b,' and ', c)
if(b>c and b>a):
    print(b,' is greater then ', a, ' and ', c)
else:
    print(c," is greater then ", a ,' and ', b)