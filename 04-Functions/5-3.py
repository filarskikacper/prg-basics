###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard_input

# Reads employee's data from keyboard
first_name = keyboard_input.input_string('Enter name: ')
last_name = keyboard_input.input_string('Enter last name: ')
age = keyboard_input.input_integer('Enter you age: ')
salary = keyboard_input.input_real('Enter your salary: ')
is_salary_hidden = keyboard_input.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name} {last_name}')
print(f'Age: {age}')
if is_salary_hidden is False:
    print(salary)