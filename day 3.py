'''
print("Welcome to the rollorcoaster")
height = int(input("What is your height?>>"))

if height >= 120:
    print("You can ride the rollorcoaster")
    age = int(input("What is your age?>>"))
    if age <= 12:
        bill = 5
        print("Please pay 5$")
    elif age <= 18:
        bill = 7
        print("please pay 7$")
    else:
        bill = 12
        print("Please pay 12$")
    with_photo = input("Do you want a photo?\nif yes y or no n>>")
    if with_photo == "y":
        bill += 3
    print(f"your total bill is {bill}$")
else:
    print("you have to taller before you can ride the rollorcoaster"

#task 2
weight = float(input("Enter your weight>>"))
height = float(input("Enter your height>>"))
bmi = weight/(height**2)

if bmi >= 25:
   print("overweight")
elif 18.5 < bmi < 25:
   print("normal weight")
else:
    print("underweight")
print(bmi)
'''






