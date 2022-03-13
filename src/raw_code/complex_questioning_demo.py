deck = {
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre'
}

for question in deck:
    user_input = input(question + ': ')
    if user_input == deck[question]:
        print('Correct!')
    else:
        print('Incorrect!')
        print('The correct answer is: ' + deck[question])
    print('---')

# output:
# un cinéma: idk
# Incorrect!
# The correct answer is: a movie theatre
# ---
# un musée: a museum
# Correct!
# ---
# un théâtre: a theatre
# Correct!
# ---
