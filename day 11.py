import random
from art import logo
def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calcullator_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_cards(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "lose! opponent ha a blackjack"
    elif u_score == 0:
        return "Congrats, you win"
    elif u_score > 21:
        return "Computer win!"
    elif c_score > 21:
        return "You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for i in range(2):
       user_cards.append(deal_cards())
       computer_cards.append(deal_cards())
    while not is_game_over:
        user_score = calcullator_score(user_cards)
        computer_score = calcullator_score(computer_cards)
        print(f"your cards: {user_cards} and your score: {user_score}")
        print(f"compyuter firs card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("choose a 'y'to get another card or choose 'n' to pass ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_cards())
        computer_score = calcullator_score(computer_cards)
    print(f"your cards: {user_cards} and your score: {user_score}")
    print(f"computers final hand {computer_cards}final score: {computer_score}")
    print(compare_cards(user_score, computer_score))
while input("Do you want to play again? (y/n) ").lower() == "y":
    print("\n" * 20)
    play_game()
