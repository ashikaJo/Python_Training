# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
"""
Creating the list
"""
x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,  7, 8, 9],600,700,800]
#x  [0,  1,  2  , 3,  4, [0,1,2,3,4,[0,  1, 2, 3, 4], 5, 6, 7, 8],5  , 6, 7]  - for my reference
# Access list: [1, 2, 3, 4]
print(x[5][:4])
# Access list: [600, 700]
print(x[-3:-1])
# Access list: [100, 300, 500, 600, 800]
print(x[::2])
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])
# Access list: [10]
print(x[5][5][0])
# Access list: [ ]
print([])


# 2. Create a list of thousand numbers using range and xrange and see the difference between each other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)
"""
Both range and xrange work the same way
xrange is used in python 2 and doesnt exist in python 3
"""
for i in range(0,1001):
    print(i)

for i in xrange(0,1001):
    print(i)

# 3. How Tuple is beneficial as compared to the list?
"""
Tuples are faster than lists, because they have a constant set of values.
Tuples are immutable. 
Elements in a tuple can be different type.
Tuples can be used as dictionary keys
"""

# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.
for i in range(1,100):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string
# with their index.
input_str = input("Enter the string here : ")
reverse_str = input_str[::-1]
vowel_ch = {'a': 1, 'e':1, 'i':1, 'o':1, 'u': 1}
print("reversed string is {}".format(reverse_str))
for i in range(len(reverse_str)):
    if reverse_str[i] in vowel_ch:
        print("vowel character in str is {} at index {}".format(reverse_str[i], i))


# 6. Write a program in Python to iterate through the string “hello my name is abcde” and
# print the string which is having an even length.
user_input = input("please enter the string here: ")
input_str = user_input.split(" ")
for i in range(0,len(input_str)):
    if len(input_str[i]) % 2 == 0:
        print(input_str[i])


# 7. Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]
# Assuming the numbers in arr are unique
arr = [1,2,3,4,5,6,7,8,9,-1]
target = 8
arr_dict = {}
output = []
for i in range(0,len(arr)):
    arr_dict[arr[i]] = 1
for i in range(len(arr)):
    if target - arr[i] in arr_dict:
        output.append([target - arr[i],arr[i]])
print(output)

# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is even,
# append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the maximum of the list.
def maxsum():
    even_list = []
    odd_list = []
    even_count = 0
    odd_count = 0
    while even_count < 5 and odd_count < 5:
        user_input = int(input("Please enter the number between 1 to 50 here: "))
        if user_input % 2 == 0:
            even_count += 1
            even_list.append(user_input)
        else:
            odd_count += 1
            odd_list.append(user_input)

    max_num = max(sum(even_list), sum(odd_list))
    print(max_num)

if __name__ == "__main__":
    maxsum()


# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

user_input = input("Please enter a string with alphanumeric characters here: ")
alpha_dict = {}
for i in range(0,len(user_input)):
    if user_input[i].isalpha():
        if user_input[i] in alpha_dict:
            alpha_dict[user_input[i]] += 1
        else:
            alpha_dict[user_input[i]] = 1
for i in alpha_dict:
    print("{} = {}".format(i, alpha_dict[i]))


# 10. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
input = (1,2,3,4,5,6,7,8,9,10)
output = []
for i in range(len(input)):
    if input[i] % 2 == 0:
        output.append(input[i])
print(tuple(output))
