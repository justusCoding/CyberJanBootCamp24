
# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20 
# Rule 2: Program must run until the correct number is guessed 
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses." 
# Rule 4: The program will tell you if your number needs to be HIGHER 
# or LOWER # until the number is guessed correctly and the program ENDS. 
# Remeber to import the random function 
#Bonus objective can you put it into a loop to make the game end after 3 turns? 
import random 
hiddenNum = random.randint(1,20) 
userNum = int(input("guess a number between 1 and 20 ")) 
numGuess = 1 
while userNum != hiddenNum : 
    if userNum > hiddenNum: 
        print("you guessed to high") 
    elif userNum < hiddenNum: 
        print("you guessed to low") 
    numGuess = numGuess + 1 
    print(userNum) 
    userNum = int(input("try again ")) 
    if userNum == hiddenNum: 
        print(f"it took you >>> {numGuess} <<< tries to get the correct number") 
        break 
    if numGuess == 3: 
        print("sorry three strikes, You're Out") 
        break

