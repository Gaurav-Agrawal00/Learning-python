a = int(input('enter the number: '))
if(a %15 == 0):
    print('number is divisible by both 3 and 5')
elif(a % 3 ==0):
    print('Number is divisible by 3')
elif(a%5 == 0 ):
    print('number is divisible by 5')
else:
    print('number is divisible by none')