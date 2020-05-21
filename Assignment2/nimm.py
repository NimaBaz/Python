"""
File: nimm.py
-------------------------
Add your comments here.
"""
NUM_STONES = 20

def main():
    # Here we will start with 20 stones and remove them till there's no more.
    milestone(NUM_STONES)

# Here we will have player 1 and 2 take turns until there are no stones
def milestone(stones):
    print("There are " + str(stones) + ("stones left"))
    # This is for player 1
    while stones >= 1:
        player1 = int(input("Player 1 would you like to remove 1 or 2 stones?"))
        while player1 > 2 or player1 < 1:
            player1 = int(input("Please enter 1 or 2: "))
        print(" ")
        stones = stones - player1
        # Here we print the amount of stones that are left and when there's no stones left we print the winner
        if stones >= 1:
            print("There are " + str(stones) + ("stones left"))
        else:
            print("Player 2 wins")
            break

        # This is player 2
        player2 = int(input("Player 1 would you like to remove 1 or 2 stones?"))
        while player1 > 2 or player1 < 1:
            player1 = int(input("Please enter 1 or 2: "))
        print(" ")
        stones = stones - player1
        # Here we print the amount of stones that are left and when there's no stones left we print the winner
        if stones >= 1:
            print("There are " + str(stones) + ("stones left"))
        else:
            print("Player 1 wins")
            break

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
