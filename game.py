"""A number-guessing game."""
import random 
"""
greet player
get player name
choose random number between 1 and 100
repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player

to-do: 
+ figure out loop
+ count # tries
- remember to randomize num
"""
print("Hello, welcome to the guessing game!")
player_name = input("What is your name? ")
rand_num = random.randint(1,100)
counter = 1

while True:
    str_num = input("Please choose a number between 1 and 100: ")
    try:
        num = int(str_num)
    except:
        print("Your entry needs to be an integer value.")
        continue 
    break

while (num >100 or num < 1):
    str_num = input("I said between 1 and 100, please. ")
    num = int(str_num)

while (num != rand_num):
    if (num < rand_num):
        print("Your guess is too low.")
    elif (num > rand_num):
        print("Your guess is too high.")
    str_num = input("Please guess another number between 1 and 100: ")
    num = int(str_num) 
    counter += 1
else:
    print(f"Congrats! You guessed the number! It took you {counter} tries!")