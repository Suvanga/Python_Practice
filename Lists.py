from ftplib import print_line

names =["Suvanga", "Hobbs", "Molyet","Sam","Carry"]
names[0]= "Suvanga Don"
print(names[0:3])
print(names)
names.pop()
print(names)

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

numbers.insert(0,"Any Type of Object")
print(numbers)

#remove an  item

numbers.remove(3)
print(numbers)

#To clear the numbers list
numbers.clear()
print(numbers)

numbers = [1,2,3,4,5]
#To check if the number exist in the list
print(1 in numbers)

# to know how many item is there in the list
print(len(numbers))
print_line("  ")

#When we want to acess each item individually and we want to erach item indiviually
#with this for loop we are going to iterate the value of the numbers in the "i" this is how we use the for loop
for i in numbers:
    print(i)

i=0
print(" ")
# We can also use this for finding the iterations
while i < len(numbers):
    print(numbers[i])
    i = i+1







