from operator import add, sub, mul, truediv

operand1 = float(input('Enter first operand: '))
operand2 = float(input('Enter second operand: '))

print('Calculator Menu\n---------------\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')

operation = input('Which operation do you want to perform? ')

if operation == '1':
    print(f'The result of the operation is {add(operand1, operand2)}. Goodbye!')
elif operation == '2':
    print(f'The result of the operation is {sub(operand1, operand2)}. Goodbye!')
elif operation == '3':
    print(f'The result of the operation is {mul(operand1, operand2)}. Goodbye!')
elif operation == '4':
    print(f'The result of the operation is {truediv(operand1, operand2)}. Goodbye!')
else:
    print('Error: Invalid selection! Terminating program.')
