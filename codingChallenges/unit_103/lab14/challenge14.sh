#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 


echo "what do you want to do today ?"
echo "1: time box all of todays work meetings"
echo "2: Run some erands"


read dayTask
if [ $dayTask = 1 ]
then
echo "how many meetings do you have today ?"
read numMeetings
echo "average meeting time? in minutes"
read avgTime
timeInMeetings=$((numMeetings * avgTime))
echo "you'll spend $timeInMeetings minutes in meetings today."
hoursInMeetings=$((timeInMeetings / 60))
    remainingMinutes=$((timeInMeetings % 60)) 
    echo "That's approximately $hoursInMeetings hours and $remainingMinutes minutes in meetings."

    timeToWork=$(( 8 - hoursInMeetings))
    echo "if you work 8 hours a day that leaves you $timeToWork hours to complete your daily work task"

elif [ $dayTask = 2 ]
then
    echo "Enter the list of errands separated by spaces:"
    read -a errandsList

    echo "You entered the following errands:"
    for errand in "${errandsList[@]}"
    do
        echo "- $errand"
    done

    totalErrandsTime=0
    for time in "${errandsList[@]}"
    do
        totalErrandsTime=$((totalErrandsTime + time))
    done
    remainingTime=$((16 * 60 - totalErrandsTime))

    remainingHours=$((remainingTime / 60))
    remainingMinutes=$((remainingTime % 60))
    
    echo "You have $remainingHours hours and $remainingMinutes minutes to complete the errands within a 16-hour workday."

else 
    echo "Not Valid"
fi