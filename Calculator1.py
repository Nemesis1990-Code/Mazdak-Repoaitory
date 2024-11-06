#Calculator!!!

while True:
    
    print(' ')
    print(' ')
    print('Calculator is at your service (^-^)')
    print(' ')

    user_input1 = input('Please enter a number or "End" to exit : ')
    print(' ')

    if user_input1.lower() == 'end':

        print('You are always welcome!')

        break

    try:

        num1 = float(user_input1)

    except ValueError:

        print('Please enter a valid number')

        continue
        
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
        
    input_operator = input('Your choice : ')

    if input_operator.lower() == 'end':

        print('You are always welcome')

        break

    if input_operator not in ['+' , '-' , '*' , '/']:
            
        print('Error! Invalid operator')

        continue

    user_input2 = input('Now give us the second number or type "End" to exit : ')

    if user_input2.lower() == 'end':

        print('You are always welcome!')

        break

    try:

        num2 = float(user_input2)

    except ValueError:
            
        print('Please enter a valid number')
    
        continue



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

            break


    print(f'The answer is: {num1} {input_operator} {num2} = {result} ')


