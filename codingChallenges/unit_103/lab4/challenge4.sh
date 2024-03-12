#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables
echo "adding 2 numbers"
read number1
read number2

function adding(){
    sum=$(( $number1 + $number2))
    echo $sum
}

adding