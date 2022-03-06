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
