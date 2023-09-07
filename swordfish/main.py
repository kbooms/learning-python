while True:
    print('Who are you?')
    name = input()
    if name != 'Broot':
        continue
    print('Hello, Kevin. What is the password?')
    password = input()
    if password == 'asdfg54321':
        break
print('Access granted.')

# asks the user their name
# if they enter anything other than the set name it continues to ask their name
# if the user enters the correct name it asks them the password
# if they enter the correct password it will tell them access granted
# if they enter the wrong password it loops back and asks their name again