name = ''
while not name:
    print('Enter your name')
    name = input()
    print('How many guests will you have?')
    numGuests = int(input())
    if numGuests:
        print('Be sure to have enough room for all your guests')
    else:
        print('Dining alone I see')
print('Done!')

# truthy and falsey values like 0, 0.0, and ""
# can be used to initiate loops