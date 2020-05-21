"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random
NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

'''
We use this while to test the variable i 10 times and we 
increment the value of i once we have our 10 random numbers
printed in the terminal. 
'''
def main():
    i = 0
    while i < 10:
        NUM_RANDOM = random.randint(0, 100)
        print(NUM_RANDOM)
        i = i + 1
    print('All done')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
