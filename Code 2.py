#calc
print('welcome to the calc')
print('pick one of the following options:')
op1=input('1 = +\n2 = -\n3 = *\n4 = /\n')
op1=int(op1)

num1=input('input number 1: ')
num1=int(num1)
num2=input('input number 2: ')
num2=int(num2)

if(op1==1):
    ans=num1 + num2
    print('the answer is: ', ans)
elif(op1==2):
    ans=num1 - num2
    print('the answer is: ', ans)
elif(op1==3):
    ans=num1 * num2
    print('the answer is: ', ans)
elif(op1==4):
    ans=num1 / num2
    print('the answer is: ', ans)
    


