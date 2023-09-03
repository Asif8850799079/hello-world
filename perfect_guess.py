# We are going to write a program that generates a random number and asks the user to guess it. If the player guess is higher than the actual number, the program displays "Lower number please". Similarly if the user's guess is too low, the program prints "higher number please"
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number 
# HINT: use the random module

import random
randomNumber = random.randint(1,100)
#print(randomNumber)
guesses = 0
userGuess = None

while(userGuess != randomNumber):
    userGuess = int(input("Enter your guess: "))
    guesses +=1
    if randomNumber==userGuess:
        print("Your guess is correct! ")
    else :
        if(userGuess>randomNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
        

print(f"You guessed the number in {guesses} guesses")

# with open("highscore.txt") as f:
#     highscore = int(f.read())

# if (guesses<highscore):
#     print("You have just broken the highscore!")
#     with open("highscore.txt",'w') as f:
#         f.write(str(guesses))