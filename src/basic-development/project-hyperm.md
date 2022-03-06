# Project: HyperM

## Introducing HyperM
Now that you've learned about packages and modules, let's dive into building another project: HyperM! Short for *hypermnesia*, a word meaning "exact recall", HyperM is a small Python script that helps you learn through digital flashcards. Just like flashcards, HyperM takes in a list of cards with "fronts" (questions) and "backs" (answers), and prompts you with each question. If you get a question wrong, it prints out the correct answer and adds the question somewhere in the deck for you to come across again later. If you get a question right, the question is removed from the deck. When you get all the questions right, the review is complete, and HyperM congratulates you.

Here's a GIF of how it looks like in action:

## The Spec
When building a project, it's important to think about the **specification, also called the spec:** the list of features and requirements for the project to be considered complete.

> 💡 It's important to make a spec before you work on a project, because you don't want to start coding and then realize you forgot about something major. 
> 
> Depending on the project, devs make specs with different levels of formality. For a basic flashcards script, a casual back-of-the-napkin bullet point list usually does the job. For larger apps with multiple teams of developers, specs can become hundreds of pages long, hammered out in meetings with complex diagrams. 
> 
> Since this is your first project where you'll be writing code independently, we'll be working through a detailed spec together so you get an idea of the exact thought process.

Let's think about what requirements there are for HyperM:

- There needs to be some way to set a "deck" of flashcards, and easily swap between different ones (so that you can swap betwen reviewing different things)
- There needs to be a way of prompting the user with a question
- There needs to be a way of checking whether the user answered said question correctly
- There needs to be a way to insert a "card" back into the deck if the user answered the question incorrectly
- There needs to be a way to show a congratulation message when the review is done

As we can see, even for something like a small flashcards script, there are quite a few things to consider.

## Design and Architecture
After making a spec, the next step in the process is figuring out how to actually implement it. Let's work through each item in the spec and think about how to actually create it (how to best add it to the app's **architecture**):

> - There needs to be some way to set a "deck" of flashcards, and easily swap between different ones (so that you can swap betwen reviewing different things)

There are a few parts of this that need to be considered carefully. The first is that the decks cannot be coded directly into the Python file, as there needs to be a way for users to swap between different decks, as well as design their own. Therefore, we need to have a way to store the flashcards data outside of the code itself.

To do this, we're going to store each flashcards deck as a **CSV** file. CSV stands for **comma-seperated values**, and it means pretty much what it says.

Consider this table:

| Term | Definition |
|------|------------|
| if statement | way of checking whether a condition is true or false |
| function | method for splitting code into another section for easy reuse |
| list | a group of items (elements) organized by order from 0 to n |

In CSV format, the above table would look like:

```csv
Term,Definition
if statement,way of checking whether a condition is true or false
function,method for splitting code into another section for easy reuse
list,a group of items (elements) organized by order from 0 to n
```

Essentially, you can think about CSVs as tables, where the columns are seperated using commas and the rows are seperated using lines.

For our use, the CSV file will look much like the table above: we'll create a CSV file per deck where the first column holds the questions and the second column holds the answers, much like the table shown above with Python terms. Python allows us to read and write to CSV files using the `csv` module in the standard library:

```py
import csv

deck_in_progress = {
	"Term": 'Definition',
	"if statement": 'way of checking whether a condition is true or false',
	"function": 'method for splitting code into another section for easy reuse',
	"list": 'a group of items (elements) organized by order from 0 to n'
}

myfile = open('myfile.csv', 'w', encoding='UTF-8')
writer = csv.writer(myfile)
for question in deck_in_progress:
    writer.writerow([question, deck_in_progress[question]])
myfile.close()

```

If we were to open up `myfile.csv`, we'd see a text file matching the CSV format shown above.

> 📖 Here, we're using Python's built in `open()` function to open a file for use. In this case, we're opening `myfile.csv` for writing (which also creates it if it doesn't exist already). Later, we'll be opening up the CSV file again to read it back. You can find out more about the `open()` function [here](https://www.geeksforgeeks.org/python-open-function/).

When we load a deck to use it in Python, we can also think of it as a dictionary. If you remember from [Chapter 1](../intro-to-code/building-blocks.md#dictionaries), we can use dictionaries to represent key-value pairs, which is exactly what a deck is.

Here's the table above again, this time represented as a Python dictionary:

```py
{
	'Term': 'Definition',
	'if statement': 'way of checking whether a condition is true or false',
	'function': 'method for splitting code into another section for easy reuse',
	'list': 'a group of items (elements) organized by order from 0 to n'
}
```

Here's an example of how we would read the deck from a CSV file on the user's computer (`myfile.csv`) and then load it as a dictionary (`deck_to_use`):

```py
myfile = open('myfile.csv', 'r', encoding='UTF-8')
reader = csv.reader(myfile)

deck_to_use = {}
for row in reader:
    deck_to_use[row[0]] = row[1]

myfile.close()

print(deck_to_use)
# output:
# {'Term': 'Definition', 'if statement': 'way of checking whether a condition is true or false', 'function': 'method for splitting code into another section for easy reuse', 'list': 'a group of items (elements) organized by order from 0 to n'}
```

**Takeaway:** when we're not using decks, we can store them as CSV files on the user's computer. When we're using a specific deck, we can load it into Python using the `csv` module and work with it as a dictionary.

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
	"if statement": 'way of checking whether a condition is true or false',
	"function": 'method for splitting code into another section for easy reuse',
	"list": 'a group of items (elements) organized by order from 0 to n'
}

for question in deck:
    user_input = input(question + ': ')
    print(user_input)
    
# output:
# if statement: I typed this input
# I typed this input
# function: I typed this too
# I typed this too
# list: And I also typed this
# And I also typed this
```

**Takeaway:** we can use the built-in `input()` function in Python to prompt the user to give an answer to a question.

> - There needs to be a way of checking whether the user answered said question correctly

Remember, at this point, we have all the questions and answers in a dictionary that we read from the CSV file:

```py
{
	'Term': 'Definition',
	'if statement': 'way of checking whether a condition is true or false',
	'function': 'method for splitting code into another section for easy reuse',
	'list': 'a group of items (elements) organized by order from 0 to n'
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
	"if statement": 'way of checking whether a condition is true or false',
	"function": 'method for splitting code into another section for easy reuse',
	"list": 'a group of items (elements) organized by order from 0 to n'
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
# if statement: way of checking whether a condition is true or false
# Correct!
# ---
# function: idk
# Incorrect!
# The correct answer is: method for splitting code into another section for easy reuse
# ---
# list: a group of items (elements) organized by order from 0 to n
# Correct!
# ---
```

**Takeaway:**

> - There needs to be a way to insert a "card" back into the deck if the user answered the question incorrectly




- [ ] Introducing Hyperm
- [ ] Explain how it works/how to build
- [ ] Push to git 
