import os

print("Hello World")

# hello world print record

print("Welcome to my first GIT repo!")

user = input("Please input directory name to verify: ")

isFile = os.path.isdir(user)
print("Does this file exist?", isFile)

if not isFile:
    print("This directory does not exist, please retry.")

