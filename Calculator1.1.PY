#Calculator!!!

while True:
    print(' ')
    print(' ')
    print('Calculator is at your service (^-^)')
    print(' ')

    while True:
        user_input1 = input('Please enter the first number or "End" to exit : ')
        print(' ')

        if user_input1.lower() == 'end':
            print('You are always welcome!')
            print(' ')
            exit()

        try:
            num1 = float(user_input1)
            break
        except ValueError:
            print('Please enter a valid number!')
            print(' ')
    
    while True:
        print('Now its time to select your operator!')
        print(' ')
        print('Enter "+" to add')
        print(' ')
        print('Or "-" to substract')
        print(' ')
        print('Or "*" to multiply')
        print(' ')
        print('Or "/" to devide')
        print(' ')
        print('And you can always enter "End" to quit')
        print(' ')

        input_operator = input('Your choise : ')
        print(' ')

        if input_operator.lower()  == 'end':
            print('You are always welcome!')
            print(' ')
            exit()
        if input_operator in ['+' , '-' , '*' , '/']:
            break
        else:
            print('Error! Invalid operator!')
            print(' ')

    while True:
        user_input2 = input('Now give us the second number : ')
        print(' ')

        if user_input2.lower() == 'end':
            print('You are always welcome!')
            print('')
            exit()
        try:
            num2 = float(user_input2)
            break
        except ValueError:
            print('please enter a valid number!')
            print(' ')
    
    if input_operator == '+':
        result = num1 + num2
    elif input_operator == '-':
        result =  num1 - num2
    elif input_operator == '*':
        result = num1 * num2
    elif input_operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print('Can not divide by zero!')
            print(' ')
            continue
    
    print(f'The answer is: {num1} {input_operator} {num2} = {result} ')
    print(' ')