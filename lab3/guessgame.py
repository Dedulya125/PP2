import random
def game():
    name = input("Hello! What is your name? \n")
    guess = 0
    num = 0
    gnum = random.randint(1, 20)
    print("Well, {fname}, I am thinking of a number between 1 and 20.\nTake a guess.".format(fname = name))
    while num != gnum:
        num = int(input())
        if num < gnum:
            guess += 1
            print("Your guess is too low.\nTake a guess.")
        elif num > gnum:
            guess += 1
            print("Your guess is too big.\nTake a guess.")
        elif guess == 3:
            print("You're out of guesses, try again")
        else:
            guess +=1
            print("Good job, {fname}! You guessed my number in {fguess} guesses!".format(fname = name, fguess = guess))
            break
game()