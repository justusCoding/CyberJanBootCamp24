#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/



echo "How is your day today? (good/bad)"
read response

case $response in
    good)
        echo "Nice, im happy for you"
        ;;
    bad)
        echo "thats rough buddy Hopefully, things will get better soon."
        ;;
    *)
        echo "invalid. Please enter good or bad"
        ;;
esac