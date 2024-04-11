#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)



echo "please enter the 3 sides of your triangle "
read userInput1
read userInput2
read userInput3

if [$userInput1 == $userInput2] && [$userInput2 == $userInput3]
then    
echo "they are all the same, EQUILATERAL"
elif [$userInput1 == $userInput2 ] && [$userInput2 != $userInput3] ||[$userInput1 != $userInput3]
then 
echo "this is ISOSCELES"
else echo " this is a SCALENE"
fi
