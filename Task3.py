# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
arr = ["1","2","python", 8, 1, 2021, 10.22, 11.3, 2+3j, 5+10j]
print(arr)

# 2. Create a list of size 5 and execute the slicing structure
list = [1,2,3,4,5]
print(list[2::])
print(list[1:3])
print(list[::4])

# 3. Write a program to get the sum and multiply of all the items in a given list.
def addMultiply(arr):
    sums = 0
    multiply = 1
    for i in range(len(arr)):
        sums += arr[i]
        multiply *= arr[i]
    return print("sum is: {} and multiplication value is : {} ".format(sums,multiply))

if __name__ == "__main__":
    addMultiply([2,3,4,5,6])

# 4. Find the largest and smallest number from a given list.
def minMax(arr):
    min_val = min(arr)
    max_val = max(arr)
    print("min_value in an arr: {} and max_val in an arr: {} ".format(min_val,max_val))

if __name__ == "__main__":
    minMax([2,3,7,8,-2])

# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
arr = eval(input("enter a list of numbers here: "))
new_list = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        new_list.append(arr[i])

print(new_list)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements
# between 1 and30 (both included).
output = []
for i in range(1,31):
    if i < 6 or i > 25:
        output.append(i**2)
print(output)

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

def replacingList(arr1,arr2):
    new_arr = []
    new_arr.append(arr1[0:len(arr1)-1] + arr2)
    print(new_arr)

if __name__ == "__main__":
    replacingList([1,3,5,7,9,10], [2,4,6,8])

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
dict1 = eval(input("enter the values of dict1 here: "))
dict2 = eval(input("enter the values of dict2 here: "))
new_dict = dict(dict1)
new_dict.update(dict2)
print("new_dict is : {}".format(new_dict))


# 9. Create a dictionary that contain numbers in the form(x:x*x)
# where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n = int(input("Enter n value here: "))
val_dict = {}
for i in range(1,n+1):
    val_dict[i] = i*i
print(val_dict)

# 10. Write a program which accepts a sequence of comma-separated numbers
# from console and generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
user_input = eval(input("please enter comma-separated numbers here: "))
list_val = list(user_input)
tuple_val = tuple(user_input)

print("list : {} and tuple: {}".format(list_val,tuple_val))