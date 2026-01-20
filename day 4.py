#import random
#random_integer = random.randint(1,10)
#print(random_integer)
##import random
#random_heads_or_tails = random.randint(0,1)
#if random_heads_or_tails == 1:
 #   print("heads")
#else:
  #  print("tails")
#import random
#friends = ('bob','akica','bakir','zokir')
#print(raandom.choice(friends))
#random_index = random.randint(0,4)
#print(friends[random_index])
import random
rock = " tosh"
paper = "qogoz"
scissor = "qaychi"

game_images = [rock,paper,scissor]
user_choice = int(input("what would you choose? type 0 for rock, 1 for paper, 2 for secissors\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
compyuter_choice = random.randint(0,2)
print("compyuter choose")
print(game_images[compyuter_choice])
if user_choice >=3 and user_choice <0:
    print("you choose invalid number")
elif user_choice == 0 and compyuter_choice == 2:
    print("you win")
elif compyuter_choice == 0 and user_choice == 2:
    print("you lose")
elif compyuter_choice > user_choice:
    print("you lose")
elif user_choice > compyuter_choice:
    print("you win")
elif compyuter_choice == user_choice:
    print("it is a draw")
