def check_correctness(guess):
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


number_of_guesses = 0
group_of_guesses = []
data = {}

correct_number = 88

while number_of_guesses < 6:
    number_of_guesses += 1

    guess = input('Guess a number between 1 and 100: ')
    print('Your guess was:')
    print(guess)

    group_of_guesses.append(guess)
    check_correctness(guess)


print('The correct number is: ')
print(correct_number)
print('Your guesses: ')
print(group_of_guesses)