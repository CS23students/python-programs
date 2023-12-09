# simple calculator
print('Simple Calculator')
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

while True:
    print('Choice: \n1.Add\n2.Sub\n3.Multiply\n4.Divide')
    ch=int(input('Select your choice: '))
    a=int(input('Enter the first number: '))
    b=int(input('Enter the second number: '))
    if ch==1:
        print(a,'+',b,'=',add(a,b))
    elif ch==2:
        print(a,'-',b,'=',sub(a,b))
    elif ch==3:
        print(a,'*',b,'=',multiply(a,b))
    elif ch==4:
        print(a,'/',b,'=',divide(a,b))
    else:
        print('Invalid input')
    ch=input('Do you want to continue (y/n): ')
    if ch=='n':
        break
   
