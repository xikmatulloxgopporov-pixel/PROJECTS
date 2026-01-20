# player_health = 10
# def game():
#     def drink_potion():
#         player_strangth = 2
#         print(player_health)
#     drink_potion()
# game()

# print(player_health)
# game_lavel = 10
# enemies = ["skeloton","zombie","aliens"]
# def create_enemy(enemy):
#     print(f"enemies inside a function{enemies}")
#     return enemy + 1
# enemies=create_enemy(enemies)
# print(f'enemies autside afunction: {enemies}')

from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("You guessed too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low.")
        return turns - 1
    else:
        print(f"you got it the answer:{actual_answer}")

def set_a_difficulty():
    level = input("Choose difficulty easy,hard:")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
def game():
    print("wellcome to the game")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"the coorect answer is {answer}")
    turns = set_a_difficulty()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} turns left.")
        user_guess = int(input("What is your guess?"))
        turns  = check_answer(user_guess, answer,turns)
    if turns == 0:
        print("Sorry, you lose.")
        return
    elif user_guess != answer:
        print("guess again")
game()

#nimadir

