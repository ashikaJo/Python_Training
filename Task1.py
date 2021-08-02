
#1.  Create three variables in a single line and assign values to them in such a manner
#    that each one of them belongs to a different data type.

a, b, c  = 1, 2.01, "Task1"


# 2. Create a variable of type complex and swap it with another variable of type integer.

a = 1 + 2j
b = 5

a = b
b = a

# 3. Swap two numbers using a third variable and do the same task without using any third variable.

a = 1
b = 2

# swapping 2 numbers using third variable
temp = a
a = b
b = temp

# swapping two numbers
a,b = b,a

# 4. Write a program that takes input from the user and prints it using both
#    Python 2.x and Python 3.x Version.

# Taking input python version 2:
# eval is used to evaluate the user input
py_v2_input  = eval(raw_input("enter a number here: "))
print(py_v2_input)
# OUTPUT :
# Enter a number here: 10+10 ; using eval will return 20;
# if not it will return 10+10

# Taking input python version 3:
py_v3_input = input("enter input here: ")
print(py_v3_input)

# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 ,
# Add the two numbers and keep the sum in another variable called z.
# Add 30 to z and store the output in variable result and print result as the final output.

user_input1 = input("enter any number between 1-10: ")
user_input2 = input("enter other number between 1-10: ")
z = user_input1 + user_input2
result = z + 30
print(result)

# 6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc

user_input = input("enter anything: ")
print("The data type of the input value is: {}".format(type(user_input)))


# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase,
#    SnakeCase and UPPERCASE. (Refer: https://capitalizemytitle.com/camel-case/)

upper_camel_case = "ConsultAdd"
lower_camel_case = "consultAdd"
snake_case = "consult_add "
upper_case = "CONSULTADD "

# 8. If one data type value is assigned to ‘a’ variable and then a different data type value
#    is assigned to ‘a’ again. Will it change the value? If Yes then Why?

"""
Ex: If the input a = 2 output for this will be 2(int) and 
when the a is assigned to a string a ="Python", then the ouput will be "Python"
 
Variables are mutable/ changable, it will always return the latest value assigned.

"""









