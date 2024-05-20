# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# :rotating_light: Don't change the code above :point_up_2:
#Write your code below this line :point_down:

print("who's turn is it to pay for the food")


print(f"it is: {random.choice(names)} turn to pay for the food")