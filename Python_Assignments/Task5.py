# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
try:
    eval("a" ++ "b")
except SyntaxError:
    print("Please correct the syntax")

# 2. Write a program in Python to allow the user to open a file by using the argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again.
# Make sure to use read only mode.
import sys
from sys import argv
def readFile():
    read_from_except = False
    while True:
        try:
            if read_from_except == True:
                file = open(user_file_name)
            else:
                file = open(argv[1])
            print(file.read())
            file.close()
            break
        except:
            read_from_except = True
            print("Entered file name is incorrect !!")
            user_file_name = input("Please enter the correct file name here: ")

if __name__ == "__main__":
    readFile()

# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
def numLengthCheck():
    while True:
        user_input = int(input("Please enter 4 digit number : "))
        try:
            if len(str(user_input)) > 4 :
                raise ValueError
        except ValueError:
            print("Input is too long !! please enter only 4 digit numbers")

        try:
            if len(str(user_input)) <= 3:
                raise ValueError
        except ValueError:
            print("Input is too short !! please enter only 4 digit numbers")


        if len(str(user_input)) == 4:
            print("Input is valid !!")
            break


if __name__ == "__main__":
    numLengthCheck()


# 4. Create a login page backend to ask users to enter the username and password.
# Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again
# but it should not be more than 3 times.
def loginPage():
    user_name = input("Please enter the username : ")
    user_password = input("Please enter the password: ")
    retype_Password = input("Please re-type the password: ")
    count = 1
    if user_password != retype_Password :

        while count <= 3:
            print("Password dint match !! You have {} attempts to enter the correct password".format(4-count))
            print("Attempt {} ".format(count))
            retype_Password = input("Please re-type the correct password: ")
            if count == 3:
                print("You have maximized your attempts. Please try again later")

            if user_password == retype_Password:
                print("Password matches !! ")
                break
            else:
                count += 1
                continue
    else:
        print("Password matches !! ")

if __name__ == "__main__":
    loginPage()

#5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling
"""
Done 
"""

#6. Read doc.txt file using Python File handling concept and return only the even length string from the file.
# Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

doc_file = open('doc.txt')
count = 0
while True:
    line = doc_file.readline()
    if not line:
        break
    elif len(line) % 2 == 0:
        count += 1
        print("Even Line {} is {} ".format(count,line.strip()))

doc_file.close()







