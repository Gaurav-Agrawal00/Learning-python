# a = input('enter your letter ')
# if(a.isupper() and a.isalpha()):
#     print('alpha is in upper case')
# else:
#     print('alpha is not in upper case')

a = input('enter your letter ')
if(a.isupper() and a.isalpha() and len(a)==1):
    print('alpha is in upper case Alphabet')
else:
    print('alpha is not in upper case Alphabet or not An alphabet')