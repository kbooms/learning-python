def spam(divideBy):
    try:
        return 42 /divideBy
    except ZeroDivisionError:
        print("Error: You'll cause a time paradox! ", end='')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
