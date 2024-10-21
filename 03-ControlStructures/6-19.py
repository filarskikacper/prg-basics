computer_science = input('SURVEY Are you interested in computer science? (y/n): ')
if computer_science == 'y':
    computer_science = 'Yes'
else:
    computer_science = 'No'
computer_games = input('Do you like playing computer games? (y/n): ')
if computer_games == 'y':
    computer_games = 'Yes'
else:
    computer_games = 'No'
instagram = input('Do you have an Instagram account? (y/n): ')
if instagram == 'y':
    instagram = 'Yes'
else:
    instagram = 'No'
print(f'SURVEY RESULTS Interested in computer science: {computer_science}')
print(f'Playing computer games: {computer_games}')
print(f'Has an Instagram account: {instagram}')