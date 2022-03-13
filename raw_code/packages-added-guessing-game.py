import random
from art import art, tprint

def check_correctness(guess): # added this <-- once again don't copy the green
    # MOVED STUFF HERE ⬇️
    hint = ''
    if int(guess) < correct_number:
        hint = 'Too small!'
    elif int(guess) > correct_number:
        hint = 'Too large!'
    elif int(guess) == correct_number:
        hint = 'Correct!'
        print(hint)
        print('Your guesses:')
        print(group_of_guesses)
        exit()
    data[guess] = hint
    print(data)

number_of_guesses = 0
group_of_guesses = []
data = {}
correct_float = random.randint(0, 100)
correct_number = int(correct_float)

tprint("Welcome to my game!", font="bulbhead")
emoticons = art("coffee", 2)
print(emoticons)

while number_of_guesses < 6:
    guess = input('Guess a number between 1 and 100: ')
    print('Your guess was:')
    print(guess)

    group_of_guesses.append(guess)

    # THE STUFF HERE GOT MOVED ABOVE ^^^
    check_correctness(guess) # added this

    number_of_guesses += 1

print('The correct number is: ')
print(correct_number)
print('Your guesses:')
print(group_of_guesses)
