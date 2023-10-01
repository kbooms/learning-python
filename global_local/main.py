# using global keyword in a function to refer to a global scope variable

def spam():
    global eggs     # global word tells python to refer to global variable 'eggs'
    eggs = "spam"   # change eggs to "spam"
eggs = "global"     # define global variable eggs equal to string 'global'
spam()              # run spam function (changes eggs variable)
print(eggs)         # show the changed variable

# commenting out the spam() function prints the original value at definition
# in this case the word "global"