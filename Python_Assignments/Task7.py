# 1. Write a program that calculates and prints the value according to the given formula: Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.
from math import sqrt
def calculateQ():
    D = input("please enter the values of D here: ").split(',')
    for i in D:
        q = sqrt((2*50*int(i))/30)
        print(q)

if __name__ == "__main__":
    calculateQ()


# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument.Both classes have an area function
# which can print the area of the shape where Shape’s area is 0 by default.

class Shape:

    def area(self,length = 0):
        self.length = length
        print("Area of shape is {}".format(self.length))

class Square(Shape):
    def __init__(self, length=0):
        self.length = length

    def area(self):
        sq_length = self.length * self.length
        print("Area of square is {}".format(sq_length))


if __name__ == "__main__":
    sh = Shape()
    sh.area()
    sq1 = Square(2)
    sq2 = Square(3)
    sq3 = Square(4)
    squares = [sq1, sq2, sq3]
    for squ in squares:
        squ.area()


# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class elements:

    def findThreeElements(arr):

        output = []
        for i in range(0, len(arr) - 2):
            for j in range(i+1, len(arr) - 1):
                for k in range(j+2, len(arr)):
                    if (arr[i] + arr[j] + arr[k]) == 0:
                        output.append([arr[i], arr[j], arr[k]])
        print(output)

if __name__ == "__main__":
    elements.findThreeElements([-25,-10,-7,-3,2,4,8,10])





# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self,time1,time2):
        self.total_hrs = time1.hours + time2.hours
        self.total_mins = time1.minutes + time2.minutes

        if self.total_mins >= 60:
            self.total_hrs += 1
            self.total_mins = self.total_mins - 60

        self.total_time = Time(self.total_hrs,self.total_mins)
        self.total_time.displayTime()

    def displayTime(self):
        print("{} hour and {} minutes".format(self.hours,self.minutes))

    def displayMinute(self):
        self.hrs_to_mins = (self.hours * 60) + self.minutes
        print("{} minutes".format(self.hrs_to_mins))


if __name__ == "__main__":
    time1 = Time(2,50)
    time2 = Time(1,20)
    time3 = Time(1,2)
    time1.addTime(time1,time2)
    time1.displayTime()
    time2.displayTime()
    time1.displayMinute()
    time2.displayMinute()
    time3.displayMinute()


# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a parameter.
# The constructor must assign the integer value to the age variable
# after confirming the argument passed is not negative;
# if a negative argument is passed then the constructor should set age to 0 and
# print “Age is not valid, setting age to 0”.
# In addition, you must write the following instance methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”. Otherwise, print “You are old”.
# Sample Input for amIOld(): -1
# 4
# 10
# 16
# 18
# 64
# 38
# Expected Output for amIOld():
# Age is not valid, setting age to 0. You are young.
# You are young.
# You are a teenager.
# You are a teenager. You are old.
# You are old.
# Consider the age variable to be set to 38 then:
# Sample Input for yearPasses(): 4
# Expected Output for yearPasses(): 42

class Person:
    def __init__(self,age):
        self.age = age
        if self.age < 0:
            print("Age is not valid, setting age to 0")
            self.age = 0

    def yearPasses(self,yearPassed):
        self.curr_age = self.age + yearPassed
        print("yearPasses {}".format(self.curr_age))


    def amIOld(self):
        if self.age >= 0 and self.age < 13:
            print("You are young !! ")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager !!! ")
        elif self.age >19:
            print("You are old. ")

if __name__ == "__main__":
    class Person:
        def __init__(self, age):
            self.age = age
            if self.age < 0:
                print("Age is not valid, setting age to 0. You are young")
                self.age = 0

        def yearPasses(self, yearPassed):
            self.curr_age = self.age + yearPassed
            print("yearPasses {}".format(self.curr_age))

        def amIOld(self):
            if self.age > 19:
                print("You are old. ")
            elif self.age >= 13 and self.age <= 19:
                print("You are a teenager !!! ")
            elif self.age > 0 and self.age < 13:
                print("You are young !! ")


    if __name__ == "__main__":
        p1 = Person(-1)
        p1.amIOld()

        p2 = Person(4)
        p2.amIOld()

        p3 = Person(10)
        p3.amIOld()

        p4 = Person(16)
        p4.amIOld()

        p5 = Person(18)
        p5.amIOld()

        p6 = Person(64)
        p6.amIOld()

        p7 = Person(38)
        p7.amIOld()

        p7.yearPasses(4)





