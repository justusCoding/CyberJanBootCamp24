# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests

user_URL = input("enter a URL you would like to send a Request to : ")

httpRequest = input("Get, Post, Put, Delete , Head, Patch, Options:")



print(f"Your Desired URL: {user_URL}")
print(f"your Desired Request: {httpRequest}")

confirm = input("Do you want to proceed? yes/no: ")
if confirm.lower() != "yes" :
    print("cancelled Request")
    exit()




response = None
if httpRequest == "Get":
    response = requests.get(user_URL)
elif httpRequest == "Post":
    response = requests.post(user_URL)
elif httpRequest == "Put":
    response = requests.put(user_URL)
elif httpRequest == "Delete":
    response = requests.delete(user_URL)
elif httpRequest == "Head":
    response = requests.head(user_URL)
elif httpRequest == "Patch":
    response = requests.patch(user_URL)
elif httpRequest == "Options":
    response = requests.options(user_URL)


if response:
    print("\nresponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
        
    print("\nResponse Status:")
    print(f"Status Code: {response.status_code}")

else :
    print("invalid Request")































