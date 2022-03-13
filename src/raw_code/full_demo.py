import random

deck = {
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre',
    'un carnaval': 'a carnival',
    'un concert': 'a concert',
    'une exposition': 'an exhibition',
    'un festival': 'a festival',
    'un musée': 'a museum',
    'un opéra': 'an opera',
    'à voir': 'must-see',
    'sensationnel': 'fantastic'
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
    print('---')
    current_index += 1

print(f'Practice session finished! You have mastered this deck! 🎉')
