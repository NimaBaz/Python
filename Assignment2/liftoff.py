"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    for num in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        print(num)
    print("Liftoff")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
