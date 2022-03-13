#################################
# NOTES:
# - remove print statements for each step as we move on
# - refactor print statements to show useful data as we move on
# - explain each concept in detail as we get to them, take questions
#################################
# This is the FIFTH section. Concept to review: loops
number_of_guesses = 0
# This is the THIRD section. Concept to review: lists
group_of_guesses = []
# This is the FOURTH section. Concepts to review: dicts
data = {}
# This is the FIRST section. Concepts to review: vars, strs, ints
correct_number = 88
# This is also part of the FIFTH section. Concept to review: loops
while number_of_guesses < 6:
    number_of_guesses += 1
    # This is the SECOND section. Concepts to review: built-in functions
    guess = input('Guess a number between 1 and 100: ')
    print('Your guess was:')
    print(guess)

    # This is also part of the THIRD section. Concept to review: lists/dicts
    group_of_guesses.append(guess)
    print(group_of_guesses)

    # This is also part of the FOURTH section. Concepts to review: dicts/if
    # statements
    ### FOR THE SIXTH SECTION, REFACTOR THE FOLLOWING INTO A FUNCTION ###
    hint = ''
    if int(guess) < correct_number:
        hint = 'Too small!'
    elif int(guess) > correct_number:
        hint = 'Too large!'
    elif int(guess) == correct_number:
        hint = 'Correct!'
    data[guess] = hint
    print(data)
    if hint == 'Correct!':
        print('=====')
        print('CORRECT!')
        print('=====')
        print('Your guesses: ')
        print(group_of_guesses)
        exit()
    ### FOR THE SIXTH SECTION, REFACTOR THE ABOVE INTO A FUNCTION ###

### Review the operators and keywords here. ###

# This is also part of the FIRST section. Concepts to review: vars, strs, ints
print('The correct number is: ')
print(correct_number)
print('Your guesses: ')
print(group_of_guesses)