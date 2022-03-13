# Project: HyperM

## Introducing HyperM
Now that you've learned about packages and modules, let's dive into building another project: HyperM! Short for *hypermnesia*, a word meaning "exact recall", HyperM is a small Python script that helps you learn through digital flashcards. Just like flashcards, HyperM takes a list of cards with "fronts" (questions) and "backs" (answers), and prompts you with each question. If you get a question wrong, it prints out the correct answer and adds the question somewhere in the deck for you to come across again later. If you get a question right, the question is removed from the deck. Once you get all the questions right, the review is complete, and HyperM congratulates you.

Here's a short video of how it looks like in action:
<script id="asciicast-wy0jUFf2E2e9VlV345mbdh581" src="https://asciinema.org/a/wy0jUFf2E2e9VlV345mbdh581.js" async></script>

## The Spec
When building a project, it's important to think about the **specification, also called the spec:** the list of features and requirements for the project.

> 💡 It's important to make a spec before you work on a project, because you don't want to start coding and then realize you forgot about something major.
> 
> Depending on the project, devs make specs with different levels of formality. For a basic flashcards script, a casual back-of-the-napkin bullet point list usually does the job. For larger apps with multiple teams of developers, specs can become [hundreds of pages long](https://www.fastcompany.com/28121/they-write-right-stuff), hammered out in meetings with complex diagrams. 
> 
> Since this is your first project where you'll be writing code independently, we'll be working through a detailed spec together so you get an idea of the exact thought process.

Let's think about what requirements there are for HyperM:

- There needs to be some way to set a "deck" of flashcards
- There needs to be a way of prompting the user with a question
- There needs to be a way of checking whether the user answered said question correctly
- There needs to be a way to insert a "card" back into the deck if the user answered the question incorrectly
- There needs to be a way to show a congratulation message when the review is done

As we can see, even for something like a small flashcards script, there are quite a few things to consider.

## Design and Architecture
After making a spec, the next step in the process is figuring out how to actually implement it. Let's work through each item in the spec and think about how to actually create it (how to best add it to the app's **architecture**):

> - There needs to be some way to set a "deck" of flashcards

Consider this table:

| Term | Definition |
|:----:|:----------:|
| un cinéma | a movie theatre |
| un musée | a museum |
| un parc d'attractions | an amusement park |
| un théâtre | a theatre |

You can think about a deck of flashcards as a table: for each card, one side is the question, while one side is the answer. So, to create flashcards in Python, we just need a simple way to represent a group of question-answer pairs. If you remember from [Chapter 1](../intro-to-code/building-blocks.md#dictionaries), we can use dictionaries to represent key-value pairs, which fits our use case: the keys can be the questions, and the values can be the answers.

Here's the table above again, this time represented as a Python dictionary:

```py
{
    'Term': 'Definition',
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre'
}
```

**Takeaway:** We can store flashcard decks as dictionaries in Python, where the key is the question and the value is the answer.

> - There needs to be a way of prompting the user with a question

This is pretty easy using Python's built-in `input()` function. We can ask for the user to input a string of text like this:

```py
>>> user_input = input('Give me some input: ')
Give me some input: I typed this sample input here
>>> print(user_input)
I typed this sample input here
>>> 
```

If we have a dictionary of questions, this is also fairly easy. We can use a [for loop](../intro-to-code/building-blocks.md#loops) to loop over each question-answer pair in the dictionary and prompt the user with the question:

```py
deck = {
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre'
}

for question in deck:
    user_input = input(question + ': ')
    print(user_input)

# output:
# un cinéma: here is some input I typed
# here is some input I typed
# un musée: here is some more input I typed
# here is some more input I typed
# un théâtre: I typed this too
# I typed this too
```

**Takeaway:** we can use the built-in `input()` function in Python to prompt the user to give an answer to a question.

> - There needs to be a way of checking whether the user answered said question correctly

Remember, we're going to store all of the questions and answers in a dictionary,
where the keys are the questions and the values are the answers:

```py
deck = {
    'un cinéma': 'a movie theatre',
    'un musée': 'a museum',
    'un théâtre': 'a theatre'
}
```

Using this, it becomes fairly easy to check whether an answer is correct. In Chapter 1, we covered [if statements](../intro-to-code/building-blocks.md#if-statements), which we can use to compare strings:

```py
answer = 'Python is awesome!'
user_input = input('Is Python awesome? ')
print('---')
if answer == user_input:
    print('YAS')
else:
    print('awww :(')

# output:
# Is Python awesome? Python is awesome!
# ---
# YAS
```

We can combine this `if` statement check with the ability to look up a value in a dictionary to ask multiple questions and mark them as **correct** or **incorrect** depending on the answer in the dictionary:

```py
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
```

**Takeaway:** we can use `if` statements to check whether a user's answers are correct or not, and we can combine them with dictionaries to check answers for each individual question.

> - There needs to be a way to insert a "card" back into the deck if the user answered the question incorrectly

If you remember [our discussion on the `random` package](https://lentoapp.github.io/code-101-with-python/basic-development/packages-and-modules.html#packages-and-modules) from Chapter 3 and [lists](https://lentoapp.github.io/code-101-with-python/intro-to-code/building-blocks.html#lists) from Chapter 1, you might already have some ideas on how we can implement this functionality.

To randomly insert an item back into the deck at some point, we can:
- create a list of questions from the dictionary's keys (we can use a function called `.keys()` to get the questions, and `list()` to turn it into a list)
- randomly pick indexes that are after the current card in the deck
- insert the question back into the list at that random index if the answer is incorrect

Here's an example of how that might look like:
```py
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
```

This is a more complex example, but don't get overwhelmed! Take some time and make sure you understand how we got each part of the code.

**Takeaway:** We can use a list of the questions, the `random` package, and the `randint()` function to randomly insert a card at some point in the deck for further review later.

> - There needs to be a way to show a congratulation message when the review is done

Last but not least, we have the congratulations message! After the previous steps, this should be pretty simple, but here are two hints:
- `print()`
- Where do you need to put the print statement so that it runs after your code finishes **loop**ing over all the cards?

## Conclusion
Congratulations! By now, you've read through a detailed spec of the project and you're ready to fully implement it on your own. Good luck, and feel free to reach out if you have any questions.
