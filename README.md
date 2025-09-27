Here is the reference review file which you can simply copy and paste to test:
# age = 12
#
# print(age)
#
# name = input("What is your name? ")
#
# print("Hello " + name )
#
#
# birth_year = input("what is your year? : ")
#
# age = 2025 - int(birth_year)
#
# print(age)
#
#
# weight = int(input("Weight: "))
# catagories = input("W (K)g or (L)bs: ")
#
# match catagories:
#     case "K" | "k" :
#         print("weight in Lbs " + str( weight*2.2))
#     case "l" | "L":
#         print("weight weight in Kgs " +str( weight/2.2))

# names =["John", "Bob", "mosh", "Suv", "Marry"]
#
# names[0] = "don"
#
# print(names[0:3])
#
# numbers =[1,2,3,4,5]
#
# numbers.insert(-2, 3)
# numbers.remove(3)
#
# print(1 in numbers)
#
# print(len(numbers))
#
#

#
# print(number)
#
# _____________________________
number = [1,2,3,4,5]
i= 0
while i < len(number) :
        print(number[i])
        i=i+1

print("instead of that we could simply use for item in number ")
for item in number:
    print(item)
# ____________________________
#now about tuples
print("use of range reference")

for items in range(5,10,2): #jumps step by 2 and also the range is from 5 to 10
    print(items)

#tuples are inmutable and they are similar to list and if you want them to not change your list then you use tuple :)

num = (1,2,3)
num.count()
