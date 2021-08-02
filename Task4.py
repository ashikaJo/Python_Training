# 1. Write a program to reverse a string. Sample input: “1234abcd” Expected output: “dcba4321”
def reverse_str(input_str):
    return print(input_str[::-1])

if __name__ == "__main__":
    reverse_str("1234abcd")
# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#Sample input: “abcSdefPghijQkl”
#Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

def findingUpperAndLowerCases(input_str):
    lower_count  = 0
    upper_count = 0
    for i in range(0,len(input_str)):
        if input_str[i].islower():
            lower_count += 1
        else:
            upper_count += 1

    print("No.of Uppercase characters: {} ; No.of Lowercase Characters: {}".format(upper_count,lower_count))

if __name__ == "__main__":
    findingUpperAndLowerCases("ashikaRoHIT")

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def uniqueElements(arr):
    map = {}
    output_arr = []
    for i in range(0,len(arr)):
        if arr[i] not in map:
            map[arr[i]] = 1
            output_arr.append(arr[i])
        else:
            continue

    return print(output_arr)

if __name__ == "__main__":
    uniqueElements([1,2,3,4,5,6,2,3,5,6,8,9])
# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
def sortedStr(input_str):
    split_str = input_str.split("-")
    sorted_str = sorted(split_str)
    output_str = "-".join(sorted_str)
    return print(output_str)

if __name__ == "__main__":
    sortedStr("a-s-h-i-k-a")

# 5. Write a program that accepts a sequence of lines as input and prints the lines
# after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
def capitalizeStr(strings):
    output = print(strings.upper())
    return output

if __name__ == "__main__":
    capitalizeStr("python training is Interesting")

# 6. Define a function that can receive two integral numbers in string form and
# compute their sum and print it in the console.
def sumOfStrs(str1,str2):
    output_sum = int(str1) + int(str2)
    return print(output_sum)

if __name__ == "__main__":
    sumOfStrs("2","5")

# 7. Define a function that can accept two strings as input and
# print the string with the maximum length in the console.
#If two strings have the same length, then the function should print both the strings line by line.
def maxLength(str1,str2):
    if len(str1) == len(str2):
        print("len of str1 : {} \nlen of str2 : {}".format(len(str1),len(str2)))
    elif len(str1) > len(str2):
        print("max len : {}".format(len(str1)))
    else:
        print("max len : {}".format(len(str2)))


if __name__ == "__main__":
    maxLength("asfgv","fghtv")
# 8. Define a function which can generate and print a tuple where the values are
# square of numbers between 1 and 20 (both 1 and 20 included).
def generateSquare():
    sq_arr = []
    for i in range(1,21):
        sq_num = i**2
        sq_arr.append(sq_num)

    print(tuple(sq_arr))

if __name__ == "__main__":
    generateSquare()

# 9. Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def showNumbers(limit):
    for i in range(0,limit+1):
        if i % 2 == 0:
            print("{}  EVEN".format(i))
        else:
            print("{}  ODD".format(i))

if __name__ == "__main__":
    showNumbers(int(input("enter the limit number here: ")))

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
def findEvenNum():
    num_list = []
    for i in range(1,21):
        num_list.append(i)
    even_num = filter(lambda x:x%2 == 0,num_list)
    print(list(even_num))
if __name__ == "__main__":
    findEvenNum()
# 11. Write a program which uses map() and filter() to make a list
# whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given list
# Use map() to generate a list of squares of the numbers in the filtered list.
# Use lambda() to define anonymous functions.
def findEvenSquareNums():
    num_list = []
    for i in range(1,11):
        num_list.append(i)
    even_num = filter(lambda x:x%2 == 0,num_list)
    even_sq_num = map(lambda x: x**2, even_num )

    print(list(even_sq_num))
if __name__ == "__main__":
    findEvenSquareNums()

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def exception(num1,num2):
    try:

        num = int(input("enter num1 here: ")) // int(input("enter num2 here: "))
    except:
        print("The divisor(num2) is invalid as its 0, try with different number")
# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
list_int = reduce(lambda x:str(x), [1,2,3,4,5,6,7])
print(list(list_int))
# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
num1 = [2,3,7,14,9]
num_not_divisible = filter(lambda x:x%3 != 0,num1)
num_multiple = filter(lambda x:x%7 == 0, num_not_divisible)
if num_not_divisible and num_multiple :
    print(list(num_multiple))

# 15. Write a program in Python to multiply the elements of a list by itself using a
# traditional function and pass the function to map() to complete the operation.
#from functools import reduce
#reduce(lambda x, y: x*y, [1,2,3,4,5,6])
def multiplication(num):
    curr_num = num
    curr_num = curr_num * num
    return curr_num
mul_map = map(multiplication,[2,3,4,5,6])
print(list(mul_map))
# 16. What is the output of the following codes:
#1.  def foo():
#       try:
#           return 1
#       finally:
#           return 2
#       k = foo()
#       print(k)
"""
output : 2
"""

#2. def a():
#       try:
#           f(x, 4)
#       finally:
#           print('after f')
#           print('after f?')
#       a()

"""
output :  f(x, 4)
NameError: name 'f' is not defined

"""



