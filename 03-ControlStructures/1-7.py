###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = 0.15 # 15%

if is_bonus == True:
    total_salary = basic_salary + bonus * 2 * basic_salary 
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {bonus * 2}')
print(f'Total salary: {total_salary}')