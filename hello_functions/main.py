import random


# define the function, indent the function code
def hello():
    print('What up!?')
    print("What's happening?")
    print("What's good?")


def number_spew():
    for i in range(10):
        spew = random.randint(0, 9)
        print(spew)


def greet(name):
    print('Hello, ' + name)


hello()
number_spew()
greet('Kevin')

# Not sure if it's the IDE or Python, but it seems to expect 2 blank lines after the end of a function definition
