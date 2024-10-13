
#adding two numbers for the tutorial  time in python

num= int(input("Weight: "))
unit = input("(K)g ir (L)bs")

if unit =="K" or unit =='k':
    print("Weight in Kg: ", int(num)//0.453)

elif unit == "l":
    num = num*0.45
    print("Weight in (L)bs: ", num)
