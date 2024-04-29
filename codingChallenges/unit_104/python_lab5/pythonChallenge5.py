# Write a program that works out whether if a given number is an 
# odd or even number
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if( number % 2 == 0) :
    print("ayeee you got an even number")
else:
    print("that aint even pal. looking pretty odd")








# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

yearBorn = int(input("What year were you born"))
monthBorn = int(input("in numbers what month were you born"))

days = ((90 - age)*365) 
weeks = ((90 - age)*52)
months = ((90 - age)*12)
print(f"you have {days} days, {weeks} weeks, and {months} months left to live if you were to reach the age of 90")

