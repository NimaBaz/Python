"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    i = 0
    # Here we print the two random generated numbers together
    while i != 3:
        num1 = ((random.randint(10, 99)))
        num2 = ((random.randint(10, 99)))
        print("What is " + str(num1) + "+" + str(num2) + "?")
        total = int(input("Your answer: "))
        if num1 + num2 == total:
            i = i + 1
            print("You've gotten ", i, "correct in a row.")
            if i == 3:
                print("Congratulations! You mastered addition.")
        else:
            i = 0
            print("Incorrect. The expected answer is ", int(num1 + num2))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
