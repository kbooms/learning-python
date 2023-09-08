# ask the user to enter a number
print("Pick a number, pal!")
loops = int(input()) + 1 # adjusted for output

# do the Fizzin and the Buzzin
print("Fizz Buzzing it!")
print("----------------")
for i in range(loops):
    if i == 0:
        continue # skip printing the 0, it comes up as FizzBuzz!
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(str(i))