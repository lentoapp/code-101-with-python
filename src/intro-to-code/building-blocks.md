# Building Blocks (~30-40 mins)

## Binary, Data, Storage, Hex, and Memory
Today, computers understand and read data that they receive through binary. Binary is a sequence of `0`'s and `1`'s, put together. From apps to videos, the data that these actions produce ultimately boils down to binary. Now, there are a lot of way binary is abstracted, or simplified, to make it easier for humans to read, understand and work with. One of these systems is called hexadecimals, or hex.

In terms of code, every program that you write will be run in the computer's memory, or RAM. So, before we get into some basic code concepts, just remember that the way your program's data gets stored in computer memory can affect certain structures or parts of your code.

Now, without further ado, here are some basic concepts and data structures you'll come across while you code!

## Variables
Variables are containers that store data for you to use in your code. For example, I created this variable `number` to have the integer value of `3`. When I add it to `7`, what's printed out is `10`.
```py
number = 3
print(number + 7)  # output: 10
```
If you want a variable to hold a certain value, such as this number, you must assign it to the variable. This is how you create variables. So here's my variable name, and this equals sign assigns the integer `7 ` to this variable. So, this variable will always have the integer value `7`, if I don't overwrite it. If I assign it again with something else, let's say `8`, the variable changes.
```py
number = 8
print(number)  # output: 8
```
It's now the integer value `8`. You can see this when I add `number` and `3` together, what's printed out is `11`.
```py
number = 8
print(number + 3)  # output: 11
```
So, variables are containers that store data and you can also overwrite them by reassigning them.

## Strings
Strings are data types that store sequences of characters, such as like `"hello world"`. To create a string in Python, you put quotation marks around the characters you want as strings:
```py
my_cool_string = 'this is some text as a Python string'
```
Strings are ordered, which means that characters are stored in a certain sequence. A character's place in this order is called an **index**. The index of the first character of a string is `0`, the next is `1`, and so on. For example, in this string "hello world", the string at index `0` is "h". At point `6`, the string is "w":
```py
my_cool_string = 'hello world'
print(my_cool_string[0])  # output: h
print(my_cool_string[6])  # output: w
```
If you want to extend or combine a string together, in python you can use the `+` sign. If you want to extend the current string that you have, you can use the `+=` sign.
```py
my_cool_string = 'hello world'
another_string = 'it is I'
a_third_string = my_cool_string + another_string
print(a_third_string)  # output: hello world it is I
my_cool_string += 'it is me'
print(my_cool_string)  # output: hello world it is me
```
This also works for numbers too:
```py
my_cool_number = 42
another_number = 81
a_third_number = my_cool_number + another_number
print(a_third_number)  # output: 123
my_cool_number += 1
print(my_cool_number)  # output: 43
```

## Lists
Lists are a type of data structure that store data in an ordered way. They are used to store and group data in a list-like form. Lists are very useful if you want to collect or store data that needs to have a specific order.
```py
my_cool_list = ['this', 'is', 'a', 'list']
```
Each item is a list is known as an **element**. Elements can be strings, integers, variables, etc. For example, if I had the variables `s0`, `s1`, and `s2` in a list called "data":
```py
s0 = "this is an element"
s1 = "another element!"
s2 = "yet again an element"
data = [s0, s1, s2]
```
`print(data[0])` would print `s0`, `print(data[1])` would print `s1`, and `print(data[2])` would print `s2`.
```py
s0 = "this is an element"
s1 = "another element!"
s2 = "yet again an element"
data = [s0, s1, s2]
print(data[0])  # output: this is an element
print(data[1])  # output: another element!
print(data[2])  # output: yet again an element
```
Once we get into loops and functions, it'll be easier for you to see how lists can be useful for collecting various types of data.

## Dictionaries
Dictionaries are a data structures that stores data in key value pairs. What does this mean? Instead of storing data in an order, dictionaries require a key for each piece of data put into it. For example, if I want to put the string "jeb" as a value in a dictionary, I would first have to make a key for it. Let's say this key is the string "reb". As in, `my_cool_dictionary['reb'] = 'jeb'`.
```py
my_cool_dictionary = {
    "a_cool_key": 'a cool value'
}
my_cool_dictionary['reb'] = 'jeb'
print(my_cool_dictionary)
# output:
# 
# my_cool_dictionary = {
#     "a_cool_key": 'a cool value'
#     "reb": 'jeb'
# }
```
Now, the useful thing about dictionaries is that they allow you to instantly look up data. For example, if I wanted to access "jeb" in this dictionary, I can just write `dict["reb"]`, as if I was look up a definition in the dictionary.
```py
my_cool_dictionary = {
    "a_cool_key": 'a cool value'
    "reb": 'jeb'
}
print(my_cool_dictionary["reb"])  # output: jeb
```
However, as much as possible, you should try not to rely on dictionaries for values that should be ordered.

## If Statements
`if` statements execute code depending on the value of a specific Boolean. A Boolean is a data type that is either `True` or `False`.

If the `if` statement evaluates a boolean to `True`, it will execute the code it leads to. However, if the `if` statement evaluates that boolean to `False`, it will not execute that code:
```py
are_pretzels_good = True
if are_pretzels_good:
    print("Agreed!")
    # the above will get run because are_pretzels_good is set to True
```
`if` statements can also lead to `elif` and `else` statements. For example, in this program, if this `if` statement is False, the program will proceed to the `elif` statement. If this `elif` statement is False, it will go to the else statement.
```py
are_pretzels_good = False
are_bananas_good = False
if are_pretzels_good:
    print("Agreed!")
    # the above won't be run
elif are_bananas_good:
    print("Alright, fair.")
    # the above won't be run
else:
    print("HERETIC")
    # the above will be run because are_pretzels_good and are_bananas_good are set to False
```

## Loops
Loops repeat a block of code over and over again. There are two types of loops, `for` loops and `while` loops. `for` loops repeat, or iterate, a block of code a certain number of times. In Python, they allow you to iterate (repeat) over data in the order that they appear in. For example, in this `for` loop, I am iterating over the `numbers` list, and `n` is each element in the `numbers` list in the order they appear in.
```py
numbers = [0, 1, 2, 3, 42]
for n in numbers:
    print(n)
# output:
# 0
# 1
# 2
# 3
# 42
```
`for` loops are very useful if you want to iterate over data, as you can access the necessary elements and the loop ends after it has iterated over each element once. In this `for` loop, I am iterating over the `numbers` list and accessing each element in `numbers` to add them up in the `sum` variable before printing it out.
```py
sum = 0
numbers = [0, 1, 2, 3, 42]
for n in numbers:
    sum += n
print(sum)  # output: 48
```

On the other hand, `while` loops keep on repeating their nested code as long as the condition you give them evaluates True. So, for example, if I say:
```py
nums = 0
while nums != 6:
    nums += 1  # this increases the value of nums each time
```
The `while` loop will keep on repeating until `nums` does equal 6. When `nums` equals 6, the loop ends. Now, you might ask, doesn't this mean that there are `while` loops that could be infinite?
And the answer to that is:
```py
while True:
    print("Pog Champ")
```
Yes.

## Operators
In languages and code, operators are symbols that tells the complier or interpreter (code reader) to perform an operation. For example, the "+" and "-" operators in Python will subtract or add integers. The "+" will also concatenate strings and lists. Below is a list of common operators in Python:

`==` \\( \rightarrow \\) 

## Keywords
Like operators, keywords are words that tells the complier or interpreter (code reader) to perform an operation. For example, `if` and `else` are keywords in Python. Below is a list of common keywords in Python:


## Functions
Functions are blocks of code that are run when they are called. For example, I can create a functions by definining, giving it a name, and writing parameters that the function accepts. Below, you write the program that the function executes. So, when the function is called, it does something to the parameters (data) according to whatever code you wrote. Functions are very useful, as you can create functions to use for various purpose. In this function, sum_it_all_up, you can see that my function takes two lists, breaks them down, and sums them both together and prints the sum. Note that the parameters aren't inherently related to lists in any way, I just treat the parameters like they are lists in my function. Therefore, if parametesr that are not list or are not all integers are passed in the function, an error from the pyhton interpreter will show up.

Python has builtin functions that are very useful and perform basic tasks. Functions are very important in Python, and will help you manipulate data. Here are some fundamental functions for programming in python: 
