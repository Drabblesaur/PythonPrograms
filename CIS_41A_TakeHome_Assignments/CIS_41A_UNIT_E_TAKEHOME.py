'''
Johnny To
CIS 41A Fall 2019
Unit E take-home assignment
'''

# First Script – Decision Making

# Write a script that can determine where different plants can be planted.
# Each plant has a name, a type (Flower, Vegetable, Tree, etc.), and a maximum height.
# There are three gardens as follows:

# 1. The Vegetable Garden can have only Vegetables, and there is no maximum height.
# 2. The Low Garden can have only Flowers, and there is a maximum height of 3.
# 3. The High Garden can have only Flowers, and there is a maximum height of 6.

# Print ONE line that identifies the one or more gardens that a given plant can be planted in.
# If a plant does not match the criteria for any of the gardens, then say so.

name = str(input("Please enter plant name: "))
type = str(input("Please enter plant type: "))
height = int(input("Please enter the height of the plant: "))
if type == "Vegetable":
    print("A", name, "can be planted in the Vegetable Garden.")
elif type == "Flower" and height <= 3:
    print("A", name, "can be planted in the Low Garden or the High Garden.")
elif type == "Flower" and height > 3:
    print("A", name, "can only be planted in the High Garden.")
else:
    print("A", name, "can not be planted in any Gardens.")

# Second Script – Guessing Game

# Write a script that plays a simple guessing game.
# The script will generate a secret number from 1 to 100, inclusive, and the user will have to guess the number.
# After each guess, the script will tell the user if they are high, low, or correct.
# If they are correct, the script will congratulate the user,
# tell them how many guesses they took, and then end the script.

import random # this generates a random integer ranging from 1-100, inclusively
secretNum = random.randint(1,100)

print("\nWelcome to the guessing game.\nYou need to guess a number from 1 to 100.")

guessNum = int(input("what is your guess? "))
counterNum = 0

while guessNum != secretNum:
    if guessNum < secretNum:
        print("Guess is too low.")
        guessNum = int(input("What is your guess? "))
        counterNum += 1
    if guessNum > secretNum:
        print("Guess is too high.")
        guessNum = int(input("What is your guess? "))
        counterNum += 1

print("Congratulations!\nYou guessed the secret number in", counterNum + 1, "guesses!")

# Third Script – has two parts

# Part One – Looping with String Methods

# a. Assign the text "Believe you can and you're halfway there." to a
#    variable called quote (this is a quote from Theodore Roosevelt).

quote = "Believe you can and you're halfway there."

# b. Loop through the quote to find and print the index of all the "a" characters.

index = 0 # initializing index variable
while index < len(quote):
    if quote[index] == "a":
        print("a found at index", index)
    index += 1

# Part Two – Nested Loops

# Write a script using nested for loops to generate a triangular multiplication table
# Ask the user how many rows they would like in their table.
# Generate formatted output where each number is right justified within a fixed field size, so that the
# numbers in each column are aligned. Test with user value of 12 rows.

numRow = int(input("Please enter the number of rows for the multiplication table: "))
i = 1
for row in range(1,numRow + 1):
    i += 1
    for column in range(1,i):
        print(row*column, end = "\t")
    print()

'''
Execution results:
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or the High Garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai can not be planted in any Gardens.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetable Garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetable Garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can only be planted in the High Garden.
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower can not be planted in any Gardens.

Welcome to the guessing game.
You need to guess a number from 1 to 100.
what is your guess? 78
Guess is too low.
What is your guess? 90
Guess is too high.
What is your guess? 80
Guess is too low.
What is your guess? 85
Guess is too high.
What is your guess? 82
Guess is too high.
What is your guess? 81
Congratulations!
You guessed the secret number in 6 guesses!
a found at index 13
a found at index 16
a found at index 28
a found at index 32
Please enter the number of rows for the multiplication table: 12
1	
2	4	
3	6	9	
4	8	12	16	
5	10	15	20	25	
6	12	18	24	30	36	
7	14	21	28	35	42	49	
8	16	24	32	40	48	56	64	
9	18	27	36	45	54	63	72	81	
10	20	30	40	50	60	70	80	90	100	
11	22	33	44	55	66	77	88	99	110	121	
12	24	36	48	60	72	84	96	108	120	132	144	
'''