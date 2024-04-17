# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
# print("yaboi jack. my favorite food curry and roti. \n dream job high 6 figures \n remote \n easy")

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
# number=int(21)
# float=21.000
# string="howdy yall"
# yesNo=bool(True)

# print the length of your string.
# print(len(string))
# print(string)
# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy = "Learning Python is Awesome!"

# Replace "Awesome" with "great" in the string
x = savvy.replace("Awesome", "great")

print(x)



# Create and assign 3 more variables called name, age and length using the multi-variable naming method.


name, age, length = "jack", 21,4

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."

miniBio = f"Hi my name is {name}, I am {length}  and {age} old today."
print(miniBio)




# Create a list of at least 5 elements of mixed data types
list = ["string", 21.00, 21, True]
print(list)

# replace a part of it with something else
list[3] = False
print(list)
# append or insert several more items to the list
list.append("mo money")
# find and print the length of the list

print(len(list))
# slice a sub-section of the 1st list, and save it to a different 2nd list
newList = list[0:3]
# print the 2nd list
print(newList)
# extend your original list with the 2nd list sliced above
list += newList
print(list)
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simList = ["ate","wax","stringy", "funny","something"]
# sort "simList", and print the list
simList.sort()
print(simList)
# copy the "simList" list to another 3rd list
copyList = simList.copy()
print(copyList)
# add the 2nd and 3rd lists together into a 4th list
extraCopyList = simList + copyList
print(extraCopyList)