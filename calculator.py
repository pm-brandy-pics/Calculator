while True:
    print('\nCalculator menu:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Divison')
    print('Exit.')
    
    choice=input('Enter your choice (1 to 5):')
    
    if choice=='1':
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))
        print('Result:',num1+num2)
    elif choice=='2':
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))
        print('Result:',num1-num2)
    elif choice=='3':
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))
        print('Result:',num1*num2)
    elif choice=='4':
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))
        if num2==0:
            print("Error! Can't divide by zero.")
        else:
            print('Result:',num1/num2)
    elif choice=='5':
        print('Exiting the calculator.')
        break
    else:
        print('Invalid input. Please enter a number between 1 and 5.')
        