"""A number-guessing game."""

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
rand_num = 32
str_num = input("Please choose a number between 1 and 100: ")
num = int(str_num)
counter = 1
while (num != rand_num):
    if (num < 32):
        print("Your guess is too low")
    elif (num > 32):
        print("You guess is too high")
    str_num = input("Please guess another number between 1 and 100: ")
    num = int(str_num) 
    counter += 1
else:
    print(f"Congrats! You guessed the number! It took you {counter} tries!")