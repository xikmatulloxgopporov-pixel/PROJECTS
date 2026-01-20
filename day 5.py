#fruits = ["apple", "banana", "cherry"]
#for fruit in fruits:
 #   print(fruit)
  #  print(fruit + "nok")
   # print(fruits)
#student_scores = [5,643,563,634,646,3666,22222,4,5,4,556,466]
#max_score = 0
#for score in student_scores:
 #   if score > max_score:
#   max_score = score
#print(max_score)
#total = 0
##for numbers in range(1,101):
  #  total += numbers
#print(total)
'''
import random
letters = ['a','s','d','d','f','g','j','k','l','p','o','y']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*']
print("GENERATE YOUR PASSWORD!")
nr_letters = int(input("enter number of letters\n"))
nr_numbers = int(input("enter number of numbers\n"))
nr_symbols = int(input("enter number of symbols\n"))
password_list=[]


for char in range(0,nr_numbers):
    password_list += random.choice(letters)

for char in range(0,nr_symbols):
    password_list += random.choice(symbols)

for char in range(0,nr_letters):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f'your final password is:{password}')
'''

