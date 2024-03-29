"""
    Day 4 of challenge 30 : class vs inheritance
    Task:
    Write a Person class with an instance variable "age", and a constructor that takes an integer - "initialAge",
    as a parameter.
    The constructor must assign "initialAge" to after confirming the argument passed as is not negative;
    if a negative argument is passed as "initialAge" , the constructor should set to 0.

    and print "Age is not valid, setting age to 0."

    In addition, you must write the following instance methods:

    1. yearPasses() should increase the instance variable by 1.
    2. amIOld() should perform the following conditional actions:
        if age < 13 : print("You are young.")
        if age > 13 and age < 18 : print("You are a teenager.")
        else: print("You are old.")
"""

class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        print("\ninitialAge: ", self.initialAge)

        if self.initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
            print("initialAge: ", self.initialAge)

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge < 13 : print("You are young.")
        elif self.initialAge >= 13 and self.initialAge < 18 :
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge += 1
        print("age in passe: ", self.initialAge)



print("Please enter the no of inputs: ")
t = int(input())
for i in range(0, t):
    print("Please enter your age: ")
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
