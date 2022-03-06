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

myfile = open('myfile.csv', 'r', encoding='UTF-8')
reader = csv.reader(myfile)

deck_to_use = {}
for row in reader:
    deck_to_use[row[0]] = row[1]

myfile.close()

print(deck_to_use)
# output:
# {'Term': 'Definition', 'if statement': 'way of checking whether a condition is true or false', 'function': 'method for splitting code into another section for easy reuse', 'list': 'a group of items (elements) organized by order from 0 to n'}
