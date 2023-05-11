# Logical Branching (if/elif/else)
# Check conditions and based on the result do something

age = int(input("Enter your age: "))

# pay attention to the indentation of the print statements within this block
# the indentation matters in python
# in the case of the if statement, the statements indented underneath it are
# executed only if the condition is true.
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18 or older to sign up")
# not indenting properly can throw an Indentation Error
# IndentationError: expected an indented block after 'if' statement on line XX

# another if statement example with strings
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# ask for the users name
name = input("Enter your name: ")
# if the user enters nothing, yell at them, otherwise greet them
if name == "":
    print("You BROKE THE RULES!")
else:
    print(f"Hello, {name}")

# use of booleans with if statements
for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = False

if online:
    print("The user is online.")
else:
    print("The user is offline.")