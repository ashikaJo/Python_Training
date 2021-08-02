# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
# number can be an integer
number = int(input("enter any number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Consultadd - Python Training")
elif number % 3 == 0:
    print("Consultadd")
elif number % 5 == 0:
    print("Python Training")


# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables
# num1 and num2 respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating
# the average as soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying
# “NEGATIVE” NOTE: At a time a user can only perform one action.

user_input = int(input("enter any 1 number from 1-5: "))
if user_input <= 5:
    num1 = int(input("enter any number: "))
    num2 = int(input("enter any number: "))

    if user_input == 1:
        add_result = num1 + num2
        if add_result < 0:
            print("Negative")
        else:
            print(add_result)

    elif user_input == 2:
        sub_result = num1 - num2
        if sub_result < 0:
            print("Negative")
        else:
            print(sub_result)

    elif user_input == 3:
        mul_result = num1 * num2
        if mul_result < 0:
            print("Negative")
        else:
            print(mul_result)

    elif user_input == 4:
        div_result = num1 // num2
        if div_result < 0:
            print("Negative")
        else:
            print(div_result)

    elif user_input == 5:
        first = int(input("enter any number: "))
        second = int(input("enter any number: "))
        avg_result = (num1 + num2 + first + second) / 4
        if avg_result < 0:
            print("Negative")
        else:
            print(avg_result)

# 3. Write a program in Python to implement the given flowchart:
print("Start")
a,b,c = 10,20,30
avg = (a+b+c) / 3
print("avg = {}".format(avg))
if avg > a and avg > b and avg >c :
    print("average is higher than a,b,c")
elif avg > a and avg > b:
    print("average is higher than a,b,c")
elif avg > a and avg > c:
    print("average is higher than a,c")
elif avg > b and avg > c:
    print("average is higher than b,c")
elif avg > a:
    print("average is higher than a")
elif avg > b:
    print("average is higher than b")
elif avg > c:
    print("average is higher than c")

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
i = 1
while i > 0:
    user_input = int(input("enter any number here: "))
    if user_input < 0:
        print("It's Over")
        break

    else:
        print("Good Going")
        continue
        i += 1

# 5. Write a program in Python which will find all such numbers which are divisible
# by 7 but are not a multiple of 5, between 2000 and 3200.
arr = []
for i in range(2000,3200):
    if i % 7 == 0 and  i % 5 != 0:
        arr.append(i)
print(arr)


# 6. What is the output of the following code examples?
#     x=123
#    for i in x:
#       print(i)
"""
output : Error msg - Since int cant be iterable 
but if we convert x to str then the i can be printed. 
"""
# i= 0
# while i < 5:
#   print(i)
#   i += 1
#   if i == 3:
#       break
#   else:
#       print(“error”)
"""
output : 0 error, 1 error , 2
"""

# count = 0
#   while True:
#      print(count)
#      count += 1
#      if count >= 5:
#         Break

"""
output : 0,1,2,3,4
"""



# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
i = 0
while i <= 6:
    if i != 3 and i != 6:
        print(i)
        i += 1
    else:
        i += 1
        continue

#  8. Write a program that accepts a string as an input from the user and calculate
#  the number of digits and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

user_input_str = input("enter any string here: ")
digit_count = 0
letter_count = 0
for i in range(len(user_input_str)):
    if user_input_str[i].isnumeric():
        digit_count += 1
    else:
        letter_count += 1

print("letters {} and Digits {}".format(letter_count,digit_count))


# 9. Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”.
# If the correct number is guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time.
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question
# whether they want to continue guessing. The program stops if the user guesses the
# correct number or answers “no”. ( The program continues as long as a user has not
# answered “no” and has not guessed the correct number)


"""
Generating the random number using randint function
Function takes 2 parameter start and end
"""
from random import randint
user_input = int(input("Guess the lucky number between 0 to 10: "))
while True:
    number = randint(0, 10)
    if user_input == number:
        print("Congratzzz !!! You have guessed the lucky number.")
        break
    else:
        print("oops !! Its not the lucky number")
        answer = input("Do you wanna continue playing ??? If so,guess the lucky number to continue "
                             "or enter no to quit ")
        if answer == "no":
            break
        else:
            continue

# 10. Write a program that asks five times to guess the lucky number.
# Use a while loop and a counter, such as
# counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not).
# If the correct number is guessed, the program outputs “Good guess!”,
# otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.

from random import randint
counter = 1
while counter < 6:
    lucky_num = randint(0, 25)
    guesses = int(input("guess the {} lucky number between 0 to 25: ".format(counter)))
    if counter == 5:
        print("Game over !")
    elif lucky_num == guesses:
        print("Good guess !")
    else:
        print("Try again !!")
    counter += 1

# 11. In the previous question, insert break after the “Good guess!” print statement.
# break will terminate the while loop so that users do not have to continue guessing after
# they found the number. If the user does not guess the number at all,
# print “Sorry but that was not very successful”.

from random import randint
counter = 1
while counter < 6:
    lucky_num = randint(0, 25)
    guesses = int(input("guess the {} lucky number between 0 to 25: ".format(counter)))
    if counter == 5:
        print("Game over !! Sorry but that was not very successful.")

    elif lucky_num == guesses:
        print("Good guess !")
        break
    else:
        print("Try again !!")

    counter += 1