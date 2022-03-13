import random

deck = {
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre'
}

list_of_questions = list(deck.keys())

current_index = 0
for question in list_of_questions:
    user_input = input(question + ': ')
    if user_input == deck[question]:
        print('Correct!')
    else:
        print('Incorrect!')
        print('The correct answer is: ' + deck[question])
        insert_point = random.randint(current_index+1, len(list_of_questions)+1)
        list_of_questions.insert(insert_point, question)
    print(list_of_questions)
    print('---')
    current_index += 1

# output:
# un cinéma: not sure
# Incorrect!
# The correct answer is: a movie theatre
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre']
# ---
# un musée: not sure tbh
# Incorrect!
# The correct answer is: a museum
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre', 'un musée']
# ---
# un cinéma: a movie theatre
# Correct!
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre', 'un musée']
# ---
# un théâtre: idk
# Incorrect!
# The correct answer is: a theatre
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre', 'un musée', 'un théâtre']
# ---
# un musée: a museum
# Correct!
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre', 'un musée', 'un théâtre']
# ---
# un théâtre: a theatre
# Correct!
# ['un cinéma', 'un musée', 'un cinéma', 'un théâtre', 'un musée', 'un théâtre']
# ---
