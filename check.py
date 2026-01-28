a = input('enter your char ')
if(a.isupper() and a.isalpha()):
    print('char is uppercase')
elif(a.islower() and a.isalpha()):
    print('char is lower case')
elif(a.isalnum() and a.isalpha()==0):
    print('char is number')
else:
    print('char is special')