# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities = 0
weekly = [0] * 4
for i, week in enumerate(monthly_expenses):
    food += week[0]
    transport += week[1]
    utilities += week[2]
    for total in week:
        weekly[i] += total
        
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',weekly[0])
print('Week 2:',weekly[1])
print('Week 3:',weekly[2])
print('Week 4:',weekly[3])
print('---------------')
print('TOTAL:',...)