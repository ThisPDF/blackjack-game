import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
cpu_cards = []


def add_cards(card_list):
    card_list.append(random.choice(cards))


for card in range(2):
    add_cards(user_cards)
    add_cards(cpu_cards)


def restart_game():
    user_cards.clear()
    cpu_cards.clear()
    for card_value in range(2):
        add_cards(user_cards)
        add_cards(cpu_cards)


def calc_total(card_list):
    total = 0
    for card_value in card_list:
        total += card_value
    return total


def choice_small(user_choice):
    if user_choice == "y":
        restart_game()
        blackjack()
    else:
        exit()


def blackjack():
    print(art.logo)
    cpu_total = calc_total(cpu_cards)
    cpu_draw = False
    if cpu_total < 17:
        print("The dealer has to draw another card. He had a total smaller than 17")
        cpu_draw = True
        add_cards(cpu_cards)
        cpu_total = calc_total(cpu_cards)
        if cpu_total > 21 and 11 in cpu_cards:
            for i in range(len(cpu_cards)):
                if cpu_cards[i] == 11:
                    cpu_cards[i] = 1
        cpu_total = calc_total(cpu_cards)
        if cpu_total > 21:
            print(f"Dealer has {cpu_total}. You win. Wanna play again? \"Y\" for yes")
            user_choice = input().lower()
            choice_small(user_choice)
    user_total = calc_total(user_cards)
    while user_total <= 21:
        print(f"You have the cards: {user_cards}.The total is: {user_total}")
        if user_total == 21:
            print("BlackJack. You Win.")
            choice_to_play = input("Do you want to play again? \"Y\" for yes\n").lower()
            choice_small(choice_to_play)
        if not cpu_draw:
            print(f"The dealer first card is: {cpu_cards[0]}")
        else:
            print(
                f"The dealer first two card are: {cpu_cards[0]} , {cpu_cards[1]}.And his total is: {cpu_total - cpu_cards[2]}")
        user_choice = input("Do you want another card? \"Y\" for yes\n").lower()
        if user_choice == "y":
            add_cards(user_cards)
            print(f"You got a: {user_cards[len(user_cards) - 1]}")
            user_total = calc_total(user_cards)
            if user_total > 21 and 11 in user_cards:
                for i in range(len(user_cards)):
                    if user_cards[i] == 11:
                        user_cards[i] = 1
                user_total = calc_total(user_cards)
            if user_total > 21:
                choice_to_play = input(
                    f"Your new total is: {user_total} witch is over 21 so you lose. Do you want to play again? \"Y\" for yes\n").lower()
                choice_small(choice_to_play)
        else:
            print(f"The dealer has {cpu_cards}. His total is {cpu_total}")
            if cpu_total < user_total:
                print("You Win")
            elif cpu_total > user_total:
                print("Dealer Wins")
            else:
                print("It's a Draw")
            choice_to_play = input("Do you want to play again? \"Y\" for yes\n").lower()
            choice_small(choice_to_play)


blackjack()
