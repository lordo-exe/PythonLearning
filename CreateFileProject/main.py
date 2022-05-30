import os

print("Hello World")

# hello world print record

print("Welcome to my first GIT repo!\n")

user = input("In order to create a file please choose a directory by name: ")

isFile = os.path.isdir(user)
print("Does this directory exist?", isFile)

if not isFile:
    print("This directory does not exist, please retry.")

if isFile:
    os.chdir(user)
    print(os.getcwd())

filename = input("Please name your text file: ")
nameExample = input("Please input your first and last name: ")
addressExample = input("Please input your full address: ")
phoneExample = input("Please input your full phone number: ")

f = open(f'{filename}.txt', 'x')
f.write(f"Name: {nameExample} \nAddress: {addressExample} \nPhone Number: {phoneExample}")
f.close()

print(f"Here are the contents of your new file named {filename}, in directory: {user}.")

f = open('exampleFile.txt', 'r')
print(f.read())

print("\nEnd of program.")