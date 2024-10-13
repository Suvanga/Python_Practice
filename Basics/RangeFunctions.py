numbers = range(5)
print(numbers)

# We need to iterate over the range object using the for loop

def print_Numbers(numbers):
    for number in numbers:
        print(number)
    print()

print_Numbers(numbers)


#To print the numbers in particular range it will use the particular boundaries, but it
# will exclude the max boundary and only include second last numer

numbers =range(5,10)
print_Numbers(numbers)


# We can also  use the range function and step numbers and we don't have to worry about stepping it up by ourselves
numbers = range(5,10,2)
print_Numbers(numbers)


# We don't need to really store the range function in the numbers variable we can directly use it in the for loop
for number in range(5):
    print(number)

