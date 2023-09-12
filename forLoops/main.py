# basic for loop formatting
for i in range(10):
    print("Basic For Loop: ", str(i + 1))
    # seems to work with or without the str() as well. Not sure if this changes the output

# break and continue can also be used in for loops
for i in range(20):
    if i % 2 == 0:
        continue
    print("Skipping the Evens: ", i)

# using an array of numbers, and calling the __contains__ method
magic_numbers = [1, 5, 10, 13, 16, 18, 21, 25]
for i in range(30):
    # __contains__ is a built-in method of Python
    if magic_numbers.__contains__(i):
        print("Magic Number reached!")
    else:
        print(i)
print("All downhill from here!")

# Start, Stop arguments of range()
for i in range(1, 31):
    if i < 4:
        print(str(i), " years, Just a baby!")
    elif i < 13:
        print(str(i), " years, an active youth!")
    elif i < 18:
        print(str(i), " years, a busy teen!")
    elif i > 18:
        print(str(i), " years, an adult!")
# Oh look, somthing a switch case would work well with

# Step argument of range(), counting by 2s
for i in range(0, 100, 2):
    print(i)