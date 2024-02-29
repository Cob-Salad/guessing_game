# Set target number, then ask the user to guess the number.
# report too high/too low until the get it
# number must be between 1-100
#
# aLimit number of tries

import getpass

from random import randint

num_of_tries = 5
num = -1
too_low = 0
too_high = 0

target_str = getpass.getpass("Enter the target number")
target = int(target_str)
#for _ in range(100):
    #target = randint(1, 100)


print(f"Guess the number between 1 and 100! You have {num_of_tries} attempts!")

while num != target and num_of_tries > 0:

    if too_low == 0 and too_high == 0:
        num = randint(1, 100)
        print(num)
        if num == target:
            print("You Win!")
        elif num <= target:
            num_of_tries = num_of_tries - 1
            too_low = too_low + 1
            print(f"+{too_low}")
            print(f"Too Low! {num_of_tries} Guesses Remaining!")
        elif num >= target:
            num_of_tries = num_of_tries - 1
            too_high = too_high + 1
            print(f"+{too_high}")
            print(f"Too High! {num_of_tries} Guesses Remaining!")

print("GAME OVER!")
print(f"The target number was {target}")





