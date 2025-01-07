"""
Task 1:
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""

def A():
    print("Hello")

def B():
    print("How are you?")

def C():
    print("Hi")


choice = input("Pick a letter: A, B, or C: ")

if choice == "A" or choice == "a":
    A()
elif choice == "B" or choice == "b":
    B()
elif choice == "C" or choice == "c":
    C()
else:
    print("invalid input")