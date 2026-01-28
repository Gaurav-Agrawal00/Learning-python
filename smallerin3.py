a= int(input('enter your first number'))
b= int(input('enter your second number'))
c= int(input('enter your third number '))
if(a<b and a<c):
    print(a,' is smaller then ', b,' and ', c)
elif(b<c and b<a):
    print(b,' is smaller then ', a, ' and ', c)
else:
    print(c," is smaller then ", a ,' and ', b)