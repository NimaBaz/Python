"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""
NUM_LENGTH = 1

def main():
    num_decreasing(NUM_LENGTH)

'''
Here I will make the user enter numbers to see how many non-decreasing numbers
they will put in. Once The number is less than the previous the program will
end with the results of the sequence.
'''
def num_decreasing(len):
    print("Enter a sequence of non-decreasing numbers.")
    num = input("Enter number: ")
    prev_num = num
    while num >= prev_num:
        num = input("Enter number: ")
        len += 1
        if num < prev_num:
            print("Thanks for playing!")
            print("Sequence length: " + len)

    # This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
