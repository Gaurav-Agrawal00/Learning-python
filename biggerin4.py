a= int(input('enter your first number'))
b= int(input('enter your second number'))
c= int(input('enter your third number '))
d= int(input('enter your fourth number '))
if(a>b and a>c and a>d):
    print(a,' is greater then ', b,' and ', c , ' and ', d)
if(b>c and b>a and b>d):
    print(b,' is greater then ', a,' and ', c , ' and ', d)
elif(c>a and c>b and c>d):
    print(c,' is greater then ', b,' and ', a , ' and ', d)
else:
    print(d,' is greater then ', b,' and ', c , ' and ', a)