# Ask for names of an individual
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

# Function that gets the first letter of a name
def get_initial(name, force_upper=True):
    if force_upper:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

print(f'Your Initials are: {get_initial(name=first_name)}{get_initial(name=middle_name)}{get_initial(name=last_name)}')
