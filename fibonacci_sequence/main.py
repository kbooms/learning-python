# each number displayed must be equal to the sum of the previous two numbers

previous_num = 0
next_num = 1
sum = 0

print('Enter the limit of the Fibonacci Sequence')
limit = int(input())

# not sure if this is cheating, but it works
print(previous_num)
print(next_num)

while sum < limit:

    sum = previous_num + next_num
    print(sum)
    previous_num = next_num
    next_num = sum

