#define the functions
def add(a,b):
    result = a+b
    return result
def  subtract(a,b):
    result = a-b
    return result
def multiply(a,b):
    result = a*b
    return result
def divide(a,b):
    result = a/b
    return result
def modulus(a,b):
    result = a%b
    return result
#list out the availabe functions
print('welcome to this simple calculator')
print('select number of operation you want to perform')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.modulus')
while True:
    operation = input('what operation number would you like to perform:')
    #check operation selected by user
    while operation !='1' and operation !='2' and operation !='3' and operation !='4' and operation !='5':
        print('invalid operation selected')
        operation = input('what operation number would you like to perform:')
        #check that numbers inputed by users are error free
    while True:
        try:
            number1 = int(input('enter first number:'))
            number2 = int(input('enter second number:'))
            break
        except ValueError:
            print('invalid input, please enter a number!')
            continue
    if operation == '1':
        print(f'{number1} + {number2} = {add(number1,number2)}')
    elif operation == '2':
        print(f'{number1} - {number2} = {subtract(number1,number2)}')
    elif operation == '3':
        print(f'{number1} X {number2} = {multiply(number1,number2)}')
    elif operation == '4':
        print(f'{number1} / {number2} = {divide(number1,number2)}')
    elif operation == '5':
        print(f'{number1} mod {number2} = {modulus(number1,number2)}')
    again = input('would you like to calculate something else? Enter yes(y) or no(n):')
    if again.lower() == 'yes' or again.lower() == 'y':
        continue
    else:
        print('thanks for using!!')
        break



