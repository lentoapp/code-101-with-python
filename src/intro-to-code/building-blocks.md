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
Lists are also a data structures that stores its data in an ordered way. They are used to store and group data in a list-like form. Lists are very useful if you want to collect or store data in a ordered way. Each item is a list is called a element. For example, if I had the variables nums, s1, and s2 in a list "data", print(data[0]) would print s1, print(data[1]) would print s2, print(data[2]), print(data[3]). Once we get into loops and function, you will be able to see more clearly how lists can be useful in collecting various types of data.

- [ ] Dictionaries
Dictionaries are a data structures that stores data in key value pairs. What does this mean? Instead of storing data in an order, dictionaries require a key for each piece of data put into it. For example, if I want to put the string "jeb" as a value in a dictionary, I would first have to make a key for it. Let's say this key is the string "reb". Ie: dict["reb"] = "jeb". Now, the useful thing with dictionaries is that its data can be instantly looked up. For example, if I wanted to access "jeb" in the dictionary, I can just write dict["reb"], as if I was look up a definiton in the dictionary. Dictionaries are not ordered.


- [ ] If Statements
If statements will execute code depending on whether it evaluates to a Boolean. A Boolean is a data type that is either True or False.

If the if statement evaluates to True, it will execute the code it leads to.
If the if statement evaluates to False, it will not execute the code it leads to.

If statements can also lead to Elif and Else statements. For example, in this program, if this if statement is False, it will go to the elif statement. If this elif statement is False, it will go to the else statement.

- [ ] Loops
Loops will repeat a block of code over and over again. There are two types of loops, for loops and while loops. For loops repeat, or iterate, a block of code a certain number of times. In Python, for loops allow you to iterate (repeat) over data in the order that they appear in. For example, in this for loop, I am iterating over the "numbers" list, and n is each element in the "numbers" list in the order they appear in. for loops are very useful if you want to iterate over data, as you can access its elements and the loop ends once it has iterated over everything. In this for loop, I am iterating over the numbers list and accessing each element in "numbers" to add them up in the "sum" variable and printing them out.

In while loops, it will keep on repeating the code under it as long as the condition you give the while loop is True. So, for example, if I say:
```py
while nums != 6:
    nums += 1
```
The while loop will keep on repeating until nums does equal 6. When nums equals 6, the loop ends. 
Now, you might ask, doesn't this mean that there are infinite while loops?
And the answer to that is:
```py
while True:
    print("Pog Champ")
```
Yes.

- [ ] Operators
In languages and code, operators are symbols that tells the complier or interpreter (code reader) to perform an operation. For example, the "+" and "-" operators in Python will subtract or add integers. The 

`==` \\( \rightarrow \\) test for equality

- [ ] Keywords
- [ ] Functions
