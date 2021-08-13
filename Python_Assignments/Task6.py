# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
def findUpperCase():
    user_input = input("Please enter a string with lower and upper case alphabets here: ")
    output = [ ch for ch in user_input if ch.isupper()]
    return output

if __name__ == "__main__":
    print(findUpperCase())

# 2. Write a program to construct a dictionary from the two lists containing
# the names of students and their corresponding subjects.
# The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
def dictOfStudentsAndClass(students,subjects):
    keyValuePairs = dict(zip(students,subjects))
    result = {name:sub for name,sub in keyValuePairs}
    return result

if __name__ == "__main__":
    print(dictOfStudentsAndClass(['Smit', 'Jaya', 'Rayyan'], ['CSE', 'Networking', 'Operating System']))
# 3. Learn More about Yield, next and Generators
"""
Done
"""


# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
def reverse_str(input_str):
    reversed_str = input_str[::-1]
    yield reversed_str

input_string = "Consultadd Training"
reversed_str = reverse_str(input_string)
for i in reversed_str:
    print(i)

# 5. Write an example on decorators.
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner

@decor1
@decor
def num():
    return 10
print(num())