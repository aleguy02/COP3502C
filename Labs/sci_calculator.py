# define necessary variables
import math

current_result = 0.0
calc_sum = 0
calc_num = 0

while True:
    # display menu
    print(f'Current Result: {current_result}\nCalculator Menu\n---------------\n'
          f'0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n'
          '6. Logarithm\n7. Display Average')

    while True:
        RESULT = current_result  # extra credit BAY BEEEEEE

        # prompt for input
        menu_selection = int(input('Enter Menu Selection: '))

        # input special cases, if input is 0, 7, or >7 or <0
        if menu_selection > 7 or menu_selection < 0:  # program continues if the menu selection is not >7 or <0
            print("Error: Invalid selection!")
            continue
        elif menu_selection == 0:  # breaks nested loop
            print("Thanks for using this calculator. Goodbye!")
            break
        elif menu_selection == 7:  # sum, num, avg of calculations
            # 1. if no calculations print message
            if calc_num == 0:
                print('Error: No calculations yet to average!')
                continue
            # 2. print sum, num, avg of calculations
            else:
                print(f'Sum of calculations: {calc_sum}\nNumber of calculations: {calc_num}'
                      f'\nAverage of calculations: {(calc_sum / calc_num):.2f}')
        else:
            break

    if menu_selection == 0:  # breaks loop, reinforces choice of nested loop above
        break

    # pick operands
    operand1 = (input('Enter first operand: '))
    operand2 = (input('Enter second operand: '))

    # EXTRA CREDIT BAY BEEEEE
    operand1 = RESULT if operand1 == 'RESULT' else float(operand1)
    operand2 = RESULT if operand2 == 'RESULT' else float(operand2)

    # doing the calculations and putting result into current_result
    if menu_selection == 1:
        current_result = operand1 + operand2
    elif menu_selection == 2:
        current_result = operand1 - operand2
    elif menu_selection == 3:
        current_result = operand1 * operand2
    elif menu_selection == 4:
        current_result = operand1 / operand2
    elif menu_selection == 5:
        current_result = operand1 ** operand2
    elif menu_selection == 6:
        current_result = math.log(operand2, operand1)

    # update sum, num of calculations
    calc_sum += current_result
    calc_num += 1

