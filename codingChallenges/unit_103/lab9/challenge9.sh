#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry



echo "enter a number 1-3"
echo "1 to print hello world" 
echo "2 ping google.com"
echo "3 to show network config"
read userInput


while [ "$userInput" != "1" ] && [ "$userInput" != "2" ] && [ "$userInput" != "3" ]
 do
    echo "Invalid entry"
    echo "Please enter a number 1-3:"
    read userInput
done

if [ $userInput = "1" ]
    then echo "Hello, World!"
elif [ $userInput = "2" ]
    then ping google.com
elif [ $userInput = "3" ]
    then ifconfig
fi


